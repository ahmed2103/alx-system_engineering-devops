#!/usr/bin/python3
"""exports data to JSON file"""
from json import dump
from requests import get

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users/").json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = get(url + "todos", params={"userId": user_id}).json()
        data[user_id] = [{"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": username} for task in todos]

    with open("todo_all_employees.json", 'w') as jsonfile:
        dump(data, jsonfile)
