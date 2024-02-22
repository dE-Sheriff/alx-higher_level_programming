#!/usr/bin/python3
"""Module: 6-load_from_json_file
"""

import json


def load_from_json_file(filename):
    """function that creates an Object from JSON file"""

    with open(filename) as file:
        data = file.read()
        return json.loads(data)
