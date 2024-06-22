#!/usr/bin/python3
"""Contains the number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://ww.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alx:0x16-api_advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

