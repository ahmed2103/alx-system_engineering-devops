#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
from requests import get


def count_words(subreddit, word_list, after=None, word_count={}):
    """parses the title of all hot articles, and prints a sorted count of given keywords"""
    response = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after),
                   headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            title = post.get('data').get('title').lower().split()
            for word in word_list:
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        after = response.json().get('data').get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        if word_count:
            for key, value in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
                print('{}: {}'.format(key, value))
        return
    print(None)
