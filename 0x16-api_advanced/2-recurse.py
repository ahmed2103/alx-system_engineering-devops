#!/usr/bin/python3
"""
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of all hot articles for a given subreddit"""
    response = get('https://www.reddit.com/r/{}/hot.json?after={}'
                   .format(subreddit, after),
                   headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
