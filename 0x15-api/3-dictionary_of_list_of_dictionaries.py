#!/usr/bin/python3
"""exports data to JSON file"""
from json import dump
from requests import get

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users/").json()
    todos = get(url + "todos").json()
    with open("todo_all_employees.json", 'w') as jsonfile:
        dump({user.get("id"): [{"task": task.get("title"),
                                "completed": task.get("completed"),
                                "username": user.get("username")} for task in todos
                               if user.get("id") == task.get("userId")]
              for user in users}, jsonfile)
