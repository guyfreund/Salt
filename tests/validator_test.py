import pytest
import os
from tools import load_json
from database import Database
from validator import Validator

samples = [sample_data for sample_data in load_json('../data/requests.json')]
valid_answers = [True, False, True, True, True, False, True, False, True, True, False, True, False, False, True, False,
                 True, False]
abnormalities_answers = [[], [{'part': 'headers', 'type': 'missing required parameter', 'field': 'Authorization'}], [],
                         [], [], [{'part': 'body', 'type': 'missing required parameter', 'field': 'firstName'}], [],
                         [{'part': 'body', 'type': 'type mismatch', 'field': 'email'}], [], [],
                         [{'part': 'query_params', 'type': 'type mismatch', 'field': 'order_id'}], [],
                         [{'part': 'body', 'type': 'type mismatch', 'field': 'order_type'}],
                         [{'part': 'body', 'type': 'missing required parameter', 'field': 'address'},
                          {'part': 'body', 'type': 'type mismatch', 'field': 'items'}], [],
                         [{'part': 'body', 'type': 'missing required parameter', 'field': 'order_id'}], [],
                         [{'part': 'body', 'type': 'type mismatch', 'field': 'order_type'}]]

answers = [t for t in zip(samples, valid_answers, abnormalities_answers)]


@pytest.mark.parametrize('sample_data, expected_valid, expected_abnormalities', answers)
def test_validate(sample_data, expected_valid, expected_abnormalities):
    database = Database(os.path.dirname(os.path.dirname(__file__)))
    database.load_models_on_init()
    validator = Validator(database)
    valid, abnormalities = validator.validate(sample_data)
    assert valid == expected_valid
    assert abnormalities == expected_abnormalities
