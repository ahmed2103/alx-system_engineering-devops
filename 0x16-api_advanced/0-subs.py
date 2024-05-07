#!/usr/bin/python3
"""Query the Reddit API and returns the number of subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Hasona'}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get('data')
    return result.get('subscribers')
