#!/usr/bin/python3
"""
This script collects information about an employee's
task list process using a REST API.
"""

import requests # type: ignore
from sys import argv


def main(employee_id):
    """Main function to gather data from the API."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Obtain employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_res = requests.get(user_url)
    user_data = user_res.json()

    # Obtain employee tasks
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task['completed']])
    employee_name = user_data['name']

    # Print progress information
    print(f"Employee {employee_name} is done with tasks("
          f"{completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(argv) == 2:
        try:
            employee_id = int(argv[1])
            main(employee_id)
        except ValueError:
            print("Please provide an integer for the employee ID.")
    else:
        print("Usage: python3 script.py <employee_id>")
