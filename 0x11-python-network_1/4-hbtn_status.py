#!/usr/bin/python3
"""
Description of module
"""
import requests


if __name__ == "__main__":
    d = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(d.text)))
    print("\t- content: {}".format(d.text))
