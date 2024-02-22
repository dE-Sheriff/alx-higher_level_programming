#!/usr/bin/python3
"""Module: Save Data to json file"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    items = []

    try:
        items = list(load_from_json_file("add_item.json"))

    except Exception:
        # len(items) == 0
        items = []

    for arg in range(1, len(argv)):
        items.append(argv[arg])

    save_to_json_file(items, "add_item.json")
