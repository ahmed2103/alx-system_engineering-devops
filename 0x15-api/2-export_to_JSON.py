#!/usr/bin/python3
"""exports data to JSON file"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todos = get(url + "todos", params={"userId": argv[1]}).json()
    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        dump({argv[1]: [{"task": task.get("title"),
                         "completed": task.get("completed"),
                         "username": user.get("username")} for task in todos]},
             jsonfile)
