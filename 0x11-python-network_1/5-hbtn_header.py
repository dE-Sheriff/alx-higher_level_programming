#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    data = requests.get(url)
    print(data.headers.get('X-Request-Id'))
