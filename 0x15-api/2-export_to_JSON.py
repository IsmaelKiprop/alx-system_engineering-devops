#!/usr/bin/python3
"""
Script to gather data from an API and export to JSON
"""

import requests
import sys
import json

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

def export_to_json(user_id, user_name, todos):
    """
    Exports TODO list to JSON file.
    """
    filename = f"{user_id}.json"

    data = {str(user_id): [{"task": task["title"], "completed": task["completed"], "username": user_name} for task in todos]}

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    user_data, todos_data = get_employee_todo_list(employee_id)
    export_to_json(user_data['id'], user_data['username'], todos_data)
