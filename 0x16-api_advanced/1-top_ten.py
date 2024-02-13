#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit """
import json
import requests
from sys import argv


def top_ten(subreddit):
    """ top_ten method """
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    u_agent = "alx-Reddit-API-project"
    header = {'User-Agent': u_agent}
    params = {"limit" : 10}

    hot_response = requests.get(url, headers=header, params=params, allow_redirects=False)

    if hot_response.status_code != 200:
        print(None)
    else:
        jsondata = hot_response.json()
        hot = jsondata.get('data').get('children')
        for new in hot:
            title = new.get('data').get('title')
            print(title)
