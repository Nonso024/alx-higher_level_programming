#!/usr/bin/python3
"""
    This script sends a request to a URL and displays the value of the
    X variable in the header of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    result = requests.get(argv[1])
    try:
        print(result.headers["X-Request-Id"])
    except KeyError:
        pass
