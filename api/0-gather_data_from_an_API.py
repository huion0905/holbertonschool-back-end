#!/usr/bin/python3
"""
This script collects information about an employee's task list process using an APIREST.
"""

import requests
from sys import argv


def main(employee_id):
    """API base URL."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Obtain employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_res = requests.get(user_url)
    user_data = user_res.json()

    # Obtain employee tasks
    all_url = f"{base_url}/all?userId={employee_id}"
    all_res = requests.get(all_url)
    all_data = all_res.json()

    # Calculate progress
    all_tasks = len(all_data)
    completed_tasks = len([task for task in all_data if task['completed']])
    employee_name = user_data['name']

    # Print progress information
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{all_tasks}):")
    for task in all_data:
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