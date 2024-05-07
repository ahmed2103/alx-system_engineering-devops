#!/usr/bin/python3
"""Query the Reddit API and returns the number of subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for subreddit"""
    response = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                   headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
