#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
     employee_id = sys.argv[1]  
     response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
     todos = response.json()
     # Get employee name
     response_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
     user_info = response_user.json()
     employee_name = user_info['name']
     
     completed_tasks = [todo for todo in todos if todo['completed']]
     num_completed_tasks = len(completed_tasks)
     total_tasks = len(todos)


     for task in completed_tasks:
         print("\"{}\",\"{}\",\"{}\",\"{}\"".format(employee_id, employee_name, todos['completed'], task['title']))