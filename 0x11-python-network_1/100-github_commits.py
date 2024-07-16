#!/usr/bin/python3
"""Description """

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{OWNER}/{REPO}/commits?per_page=10' \
        .format(OWNER=owner_name, REPO=repo)
    api_token = ''
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer {YOUR_TOKEN}'.format(YOUR_TOKEN=api_token),
        'X-GitHub-Api-Version': '2022-11-28'
    }
    r = requests.get(url)
    response = r.json()
    for i in response[:10]:
        print('{}: {}'.format(i['sha'], i['commit']['author']['name']))
