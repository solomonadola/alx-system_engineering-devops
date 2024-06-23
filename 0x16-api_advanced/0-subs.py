#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyApp v1.0 by u/Silver_Oil1466'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0