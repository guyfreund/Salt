import logging
from typing import Tuple

from database import Database
from model import Model
from sample import Sample
from constants import TYPE_MISMATCH, MISSING_REQUIRED, HEADERS, BODY, QUERY_PARAMS, PART, FIELD, TYPE, POSSIBLE_TYPES, \
    TYPES


class Validator:
    """
    A class that validates given samples of requests

    Args:
        database (Database): the database to retrieve the models for validation

    """

    def __init__(self, database: Database):
        self.database = database
        self.temp_abnormalities: list = []

    def validate(self, sample_data: dict) -> Tuple[bool, list]:
        """ Retrieves the corresponding model of the sample and returns the validation result

        Args:
            sample_data (dict): the sample data

        Returns:
            bool: the validation result
            list: the list of abnormalities

        """
        self.temp_abnormalities = []
        sample: Sample = Sample(sample_data)
        model: Model = self.database.get_model_by_path(sample.path)

        if not model:
            error_msg: str = f'No model with path {sample.path} was found in db.'
            logging.exception(f'Validator error: {error_msg}')
            raise Exception(error_msg)

        return self.is_valid(model, sample), self.temp_abnormalities

    def is_valid(self, model: Model, sample: Sample) -> bool:
        """ Validates a sample according to its corresponding model

        Args:
            model (Model): the model
            sample (Sample): the sample data

        Returns:
            bool: True if the sample is abnormal, False otherwise

        """
        no_missing_required: bool = self.no_missing_required(model, sample)
        no_type_mismatches: bool = self.no_type_mismatches(model, sample)
        return no_missing_required and no_type_mismatches

    def no_missing_required(self, model: Model, sample: Sample) -> bool:
        """ Ensures that a sample has all the required params for every request part

        Args:
            model (Model): the model
            sample (Sample): the sample data

        Returns:
            bool: True if the sample is abnormal, False otherwise

        """
        return all([
            self.no_missing_required_generic_request_part(
                model.headers.required_fields, sample.headers.fields.keys(), HEADERS
            ),
            self.no_missing_required_generic_request_part(
                model.body.required_fields, sample.body.fields.keys(), BODY
            ),
            self.no_missing_required_generic_request_part(
                model.query_params.required_fields, sample.query_params.fields.keys(), QUERY_PARAMS
            ),
        ])

    def no_missing_required_generic_request_part(self, model_required_fields: set, sample_fields: set, part: str) -> \
            bool:
        """ Ensures no missing required fields in the sample's field

        Args:
            model_required_fields (set): the model's part required fields
            sample_fields (set): the sample's part fields
            part (str): the part being checked

        Returns:
            True if there's a missing field, False otherwise

        """
        diff: set = model_required_fields - sample_fields

        for missing_field in diff:
            self.temp_abnormalities.append({PART: part, TYPE: MISSING_REQUIRED, FIELD: missing_field})

        return True if not diff else False

    def no_type_mismatches(self, model: Model, sample: Sample) -> bool:
        """ Ensures that a sample has no type mismatches in its headers, body & query_params

        Args:
            model (Model): the model
            sample (Sample): the sample data


        Returns:
            bool: True if the sample is abnormal, False otherwise

        """
        return all([
            self.no_type_mismatches_generic_request_part(model.headers.fields, sample.headers.fields, HEADERS),
            self.no_type_mismatches_generic_request_part(model.body.fields, sample.body.fields, BODY),
            self.no_type_mismatches_generic_request_part(
                model.query_params.fields, sample.query_params.fields, QUERY_PARAMS
            )
        ])

    def no_type_mismatches_generic_request_part(self, model_part_fields: dict, sample_part_fields: dict, part: str) -> \
            bool:
        """ Ensures that a sample's generic request part has no type mismatches

        Args:
            model_part_fields (dict): the model part fields
            sample_part_fields (dict): the sample part fields
            part (str): the part being checked

        Returns:
            bool: True if the sample is abnormal, False otherwise

        """
        answer: bool = True

        for field_name, field in sample_part_fields.items():
            model_field: dict = model_part_fields.get(field_name)
            if not model_field:
                continue

            model_field_types: set = set(model_field.get(TYPES, []))
            sample_field_possible_types: set = field.get(POSSIBLE_TYPES)
            if not sample_field_possible_types or not model_field_types.intersection(sample_field_possible_types):
                answer = False
                self.temp_abnormalities.append({PART: part, TYPE: TYPE_MISMATCH, FIELD: field_name})

        return answer
