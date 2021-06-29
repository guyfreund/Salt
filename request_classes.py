from typing import Dict

from tools import find_types
from constants import POSSIBLE_TYPES, VALUE, REQUIRED, NAME


class GenericRequestPart:
    def __init__(self, data):
        self.data: list = data
        self.fields: Dict[str, dict] = {}
        for field in data:
            field.update({POSSIBLE_TYPES: find_types(field.get(VALUE))})
            self.fields[field.get(NAME)] = field


class GenericModelRequestPart(GenericRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)
        self.required_fields: set = {field.get(NAME) for field in data if field.get(REQUIRED, False)}


class Body(GenericRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)


class Headers(GenericRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)


class QueryParams(GenericRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)


class ModelBody(GenericModelRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)


class ModelHeaders(GenericModelRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)


class ModelQueryParams(GenericModelRequestPart):
    def __init__(self, data: dict):
        super().__init__(data)
