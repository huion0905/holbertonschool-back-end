#!/usr/bin/python3
"""This script collects information about an employee's task list process using an APIREST."""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        employee_id = argv[1]
        """Replace 'BASE_URL' with the actual URL of the API to be queried"""
        BASE_URL = "https://jsonplaceholder.typicode.com"

        """Obtain employee information"""
        user_url = f"{BASE_URL}/users/{employee_id}"
        user_response = requests.get(user_url)
        employee_name = user_response.json().get('name')

        """Obtain all tasks associated with the employee"""
        todos_url = f"{BASE_URL}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        """Calculate the number of tasks completed and totals"""
        total_tasks = len(todos)
        done_tasks = sum(task['completed'] for task in todos)

        """Print progress information"""
        message = (
            f"Employee {employee_name} is done with tasks"
            f"({done_tasks}/{total_tasks}):"
        )
        print(message)

        """Print the titles of completed tasks"""
        for task in todos:
            if task['completed']:
                print(f"\t {task['title']}")
