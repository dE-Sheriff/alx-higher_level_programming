#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    from urllib import request
    import sys

    address = sys.argv[1]
    with request.urlopen(request.Request(address)) as connection:
        print(dict(connection.getheaders()).get('X-Request-Id'))
