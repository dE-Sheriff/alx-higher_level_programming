#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    from urllib import request, parse
    import sys

    server = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('ascii')
    req = request.Request(server, data=data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
