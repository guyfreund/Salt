from request_classes import Body, Headers, QueryParams
from constants import PATH, METHOD, HEADERS, QUERY_PARAMS, BODY


class Sample:
    """
    A class that represents a sample of a request performed to a specific API endpoint

    Args:
        data (dict): the model's data
        path (str): the model's endpoint (path)
        method (str): the model's method
        headers (Headers): the model's list of known headers values
        body (Body): the model's list of known body values
        query_params (QueryParams): the model's list of known query params values

    """
    def __init__(self, model_data: dict):
        self.data: dict = model_data
        self.path: str = model_data[PATH]
        self.method: str = model_data.get(METHOD)
        self.headers: Headers = Headers(model_data.get(HEADERS, []))
        self.body: Body = Body(model_data.get(BODY, []))
        self.query_params: QueryParams = QueryParams(model_data.get(QUERY_PARAMS, []))
