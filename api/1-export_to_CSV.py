#!/usr/bin/python3
import requests
import csv
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        employee_id = argv[1]
        """Replace 'BASE_URL' with the actual URL of the API to be queried"""
        BASE_URL = "https://jsonplaceholder.typicode.com"

        """Obtain employee information"""
        user_url = f"{BASE_URL}/users/{employee_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')
        username = user_data.get('username')

        """Obtain all tasks associated with the employee"""
        todos_url = f"{BASE_URL}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                csvwriter.writerow([employee_id, username, task['completed'], task['title']])
