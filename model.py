from request_classes import ModelBody, ModelHeaders, ModelQueryParams
from constants import PATH, METHOD, HEADERS, QUERY_PARAMS, BODY


class Model:
    """
    A class that represents a model of an API endpoint

    Args:
        data (dict): the model's data
        path (str): the model's endpoint (path)
        method (str): the model's method
        headers (ModelHeaders): the model's list of known headers values
        body (ModelBody): the model's list of known body values
        query_params (ModelQueryParams): the model's list of known query params values

    """
    def __init__(self, model_data: dict):
        self.data: dict = model_data
        self.path: str = model_data[PATH]
        self.method: str = model_data.get(METHOD)
        self.headers: ModelHeaders = ModelHeaders(model_data.get(HEADERS, []))
        self.body: ModelBody = ModelBody(model_data.get(BODY, []))
        self.query_params: ModelQueryParams = ModelQueryParams(model_data.get(QUERY_PARAMS, []))
