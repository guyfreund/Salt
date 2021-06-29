import pytest
import os
from tools import load_json
from database import Database
from constants import MODELS_PATH

models = [model_data for model_data in load_json(f'../{MODELS_PATH}')]


@pytest.mark.parametrize('model', models)
def test_load_models_on_init(model):
    database = Database(os.path.dirname(os.path.dirname(__file__)))
    assert database.get_model_by_path(model['path'])


def test_add_model():
    database = Database(os.path.dirname(os.path.dirname(__file__)))
    database.load_models_on_init()
    model_data = models[0]
    model_data['path'] = 'test_path'
    database.add_model(model_data)
    assert 'test_path' in database.models
