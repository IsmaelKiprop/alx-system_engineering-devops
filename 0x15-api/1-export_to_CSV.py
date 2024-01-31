#!/usr/bin/python3
"""
Script to gather data from an API and export to CSV
"""

import requests
import sys
import csv

def get_employee_todo_list(employee_id):
    """
    Retrieves and returns employee TODO list progress from the API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        return user_data, todos_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(user_id, user_name, todos):
    """
    Exports TODO list to CSV file.
    """
    filename = f"{user_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for task in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    user_data, todos_data = get_employee_todo_list(employee_id)
    export_to_csv(user_data['id'], user_data['username'], todos_data)
