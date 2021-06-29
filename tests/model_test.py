import pytest
from model import Model
from tools import load_json

models = load_json('../data/models.json')


@pytest.mark.parametrize('model_data', models)
def test_init(model_data):
    model = Model(model_data)
    assert model.data
    assert model.path
    assert model.method
    assert model.headers is not None
    assert model.body is not None
    assert model.query_params is not None
    assert model.auth is not None
