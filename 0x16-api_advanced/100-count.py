#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
from requests import get


def count_words(subreddit, word_list, after=None, word_count={}):
    """parses the title of all hot articles, and prints a sorted
    count of given keywords"""
    response = get('https://www.reddit.com/r/{}/hot.json?after={}'
                   .format(subreddit, after),
                   headers={'User-Agent': 'hasona'})
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
            for key, value in sorted(word_count.items(),
                                     key=lambda x: x[1], reverse=True):
                print('{}: {}'.format(key, value))
        return
    print(None)
"""
100-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])