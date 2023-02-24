#!/usr/bin/python3
"""
From task #0, extending the Python script to export data in the JSON format.
"""


import json
import requests
import sys


"""Importing libraries"""


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_data = requests.get(todos_url).json()

    employee_username = requests.get(users_url).json()["username"]

    info = []
    result = {user_id: info}

    for todo in todo_data:
        if user_id == todo["userId"]:
            info.append(
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_username
                }
            )

    print(result)
    file = "{}.json".format(user_id)
    with open(file, 'w') as files:
        json.dump(result, files)
