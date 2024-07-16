#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    server = 'http://0.0.0.0:5000/search_user'
    search = sys.argv[1] if len(sys.argv) > 1 else ""

    post = {"q": search}
    req = requests.post(server, data=post)
    try:
        response = req.json()
        if response != {}:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
