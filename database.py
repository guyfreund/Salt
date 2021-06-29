import logging
import os
from typing import Dict, Union

from model import Model
from tools import load_json
from constants import MODELS_PATH


class Database:
    """
    A class that represents a Database of models

    Args:
        db_root_path (str): the path to the root of the database
        models (Dict[str, Model]): a mapping from model path to corresponding Model object

    """

    def __init__(self, db_root_path: str):
        self.db_root_path: str = db_root_path
        self.models: Dict[str, Model] = {}
        # self.load_models_on_init()

    def load_models_on_init(self):
        """ Loads existing models on init - just for testing """
        raw_models_list: list = load_json(os.path.join(self.db_root_path, MODELS_PATH))
        for model_data in raw_models_list:
            self.add_model(model_data)

    def add_model(self, model_data: dict):
        """ Adds a model to the database

        Args:
            model_data (dict): The model data

        """
        model: Model = Model(model_data)
        self.models.update({model.path: model})

    def get_model_by_path(self, path: str) -> Union[Model, None]:
        """ Returns a model by a given path

        Args:
            path (str): the path to retrieve the model by

        Returns:
            Model: the model if exists, None otherwise

        """
        model: Model = self.models.get(path)
        if not model:
            logging.debug(f'No model with path {path} was found in db.')

        return model
