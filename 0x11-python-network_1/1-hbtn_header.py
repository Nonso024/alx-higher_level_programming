#!/usr/bin/python
"""Script that:
- takes in a url,
- sends a request to the url and displsys the value
- of the X-Request-Id variable found in the header of thr reponse.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
