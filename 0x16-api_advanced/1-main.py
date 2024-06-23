#!/usr/bin/python3
"""
1-main
This script uses the `top_ten` function from
`1-top_ten` module to fetch and print
the titles of the first 10 hot posts of a given subreddit.
"""

import sys


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
