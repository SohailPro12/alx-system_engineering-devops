#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()

    params = {"userId": emp_id}
    todos = requests.get(url + "todos", params).json()

    completed = [todo.get("title") for todo in todos if todo.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(complete)) for complete in completed]
