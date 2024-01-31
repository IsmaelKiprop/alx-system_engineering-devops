#!/usr/bin/python3
"""
Export data in JSON format for all tasks from all employees
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # API base URL
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch users
    users_url = base_url + "users"
    users_response = requests.get(users_url)
    users = users_response.json()

    # Fetch tasks
    tasks_url = base_url + "todos"
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Dictionary to store tasks for each user
    tasks_dict = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Filter tasks for the current user
        user_tasks = [
            {"username": username, "task": task["title"], "completed": task["completed"]}
            for task in tasks
            if task["userId"] == user["id"]
        ]

        # Store user tasks in the dictionary
        tasks_dict[user_id] = user_tasks

    # Export to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as json_file:
        json.dump(tasks_dict, json_file)
