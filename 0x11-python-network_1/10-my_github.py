#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    server = 'https://api.github.com/user'
    username = sys.argv[1]  # peterchibunna
    password = sys.argv[2]  # ghp_b49e787f2cfa428f89927175ab0c2b1b

    r = requests.get(server, auth=(username, password))
    response = r.json()
    print(response.get('id', None))
