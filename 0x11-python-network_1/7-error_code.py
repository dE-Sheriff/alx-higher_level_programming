#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code == 200:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))
