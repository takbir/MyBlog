# encoding=utf8

import json


def is_jsonable(json_str):
    try:
        json.loads(json_str)
    except ValueError:
        return False
    return True
