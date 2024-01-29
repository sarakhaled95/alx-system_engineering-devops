#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    names = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    id_dict = {}
    username_dict = {}

    for user in names:
        emp_id = user.get("id")
        id_dict[emp_id] = []
        username_dict[emp_id] = user.get('username')
    for task in todos:
        mydict = {}
        emp_id = task.get('userId')
        mydict["task"] = task.get('title')
        mydict["completed"] = task.get('completed')
        mydict["username"] = username_dict.get(emp_id)
        id_dict.get(emp_id).append(mydict)

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(id_dict, jsonfile)
