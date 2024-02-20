#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress 
and exports it in CSV format.
"""

import json
import requests
import sys

if __name__ == "__main__":

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    response = requests.get('{}/todos?userId={}'.format(
                            BASE_URL, employee_id))
    todos = response.json()

    response_user = requests.get('{}/users/{}'.format(
                            BASE_URL, employee_id))
    user_info = response_user.json()
    employee_name = user_info['name']

    data = {
        employee_id: [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            for todo in todos
        ]
    }


    filename = '{}.csv'.format(employee_id)

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
