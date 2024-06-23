#!/usr/bin/python3
"""
Module to query the Reddit API and
get the number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    the function returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "v1.0 (by /u/Silver_Oil1466)"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
