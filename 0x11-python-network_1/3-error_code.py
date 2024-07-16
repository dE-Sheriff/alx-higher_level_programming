#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    from urllib import request, parse, error
    import sys

    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            print(data)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
