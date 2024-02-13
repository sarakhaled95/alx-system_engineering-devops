#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers"""
import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """number of subscriber method"""
    subreddit = argv[1]
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    agent_string = "API-practice-alx-cardano"
    header = {'User-Agent': agent_string}
    subs = requests.get(url, headers=header, allow_redirects=False)
    if subs.status_code != 200:
        return (0)
    else:
        json_response = subs.json()
        sub_count = json_response.get('data').get('subscribers')
        return sub_count
