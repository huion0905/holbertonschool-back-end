#!/usr/bin/python3
"""
Script to export data into the CSV format.
"""

import requests
import csv
from sys import argv


def main(employee_id):
    """Main function to gather data from the API and save it to a CSV file"""
    base_url = "https://jsonplaceholder.typicode.com"

    # Obtain employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_res = requests.get(user_url)
    user_data = user_res.json()
    username = user_data['username']

    # Obtain employee tasks
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    # Create a CSV file and write the data
    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write each task to the CSV
        for task in todos_data:
            task_writer.writerow([employee_id, username, task['completed'], task['title']])


if __name__ == '__main__':
    if len(argv) == 2:
        try:
            employee_id = int(argv[1])
            main(employee_id)
        except ValueError:
            print("Please provide an integer for the employee ID.")
    else:
        print("Usage: python3 script.py <employee_id>")
