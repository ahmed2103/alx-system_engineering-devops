#!/usr/bin/python3
"""Query the Reddit API and returns the hottest ten posts"""
from requests import get


def top_ten(subreddit):
    """Returns the top ten posts for subreddit"""
    response = get('https://www.reddit.com/r/{}/hot.json'
                   .format(subreddit),
                   params={'limit': 10},
                   headers={'User-Agent': 'hasona'},
                   allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
        return
    print("None")
