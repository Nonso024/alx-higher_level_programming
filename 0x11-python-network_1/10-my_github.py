#!/usr/bin/python3
"""
Scrtpt that takes a user's Github credentials and
uses the GitHub API to dsiplay the users id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    headers = {
        "Authorization": "Bearer {}".format(argv[2]),
        "X-GitHub-Api-Version": "2022-11-28"
    }
    res = requests.get("https://api.github.com/user", headers=headers)
    try:
        print(res.json()["id"])
    except KeyError:
        print(None)
