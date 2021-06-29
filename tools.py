import json
import os
import re
from typing import Any

from constants import AUTH_TOKEN_REGEX, UUID_REGEX, DATE_REGEX, EMAIL_REGEX, STRING, LIST, BOOLEAN, INT, DATE, UUID, \
    EMAIL, AUTH_TOKEN


def load_json(file_path: str) -> list:
    """ Reads and loads json file.

    Args:
        file_path (str): full path to json file.

    Returns:
        list: loaded json file.

    """
    try:
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                result = json.load(json_file)
        else:
            result = []
        return result
    except json.decoder.JSONDecodeError:
        return []


def find_types(value: Any) -> set:
    """ Finds the possible types of a given value

    Args:
        value: the value

    Returns:
        list: the list of possible types

    """
    types: set = set()

    if value is not None:
        if isinstance(value, list):
            types.add(LIST)

        if isinstance(value, bool):
            types.add(BOOLEAN)

        if isinstance(value, int):
            types.add(INT)

        if isinstance(value, str):
            if re.match(DATE_REGEX, value):
                types.add(DATE)

            if re.match(UUID_REGEX, value):
                types.add(UUID)

            if re.match(AUTH_TOKEN_REGEX, value):
                types.add(AUTH_TOKEN)

            if re.match(EMAIL_REGEX, value):
                types.add(EMAIL)

            types.add(STRING)

    return types
