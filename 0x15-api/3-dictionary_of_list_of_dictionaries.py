#!/usr/bin/python3
"""exports data to JSON file"""
from json import dump
from requests import get

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users/").json()
    todos = get(url + "todos").json()
    data = {}
    for user in users:
        data[user.get("id")] = [{"username": user.get("username"),
                                 "task": task.get("title"),
                                 "completed": task.get("completed")}
                                for task in todos if task.get("userId") == user.get("id")]
    with open("todo_all_employees.json", 'w') as jsonfile:
        dump(data, jsonfile)
