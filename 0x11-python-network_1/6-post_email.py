#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    server = sys.argv[1]
    email = sys.argv[2]
    post = {'email': email}

    req = requests.post(server, data=post)
    print(req.text)
