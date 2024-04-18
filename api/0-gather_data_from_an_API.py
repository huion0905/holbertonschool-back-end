#!/usr/bin/python3
"""Module to interact with an api"""
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    response_todos = requests.get(f"{url}/todos?userId={sys.argv[1]}")
    response_users = requests.get(f"{url}/users/{sys.argv[1]}")

    todos = response_todos.json()
    user = response_users.json().get('name')

    done_taks = list()
    for todo in todos:
        if todo.get('completed'):
            done_taks.append(todo)
    print(
        f"Employee {user} is done with tasks({len(done_taks)}/{len(todos)}):")
    for todo in done_taks:
        print(f"\t {todo.get('title')}")
