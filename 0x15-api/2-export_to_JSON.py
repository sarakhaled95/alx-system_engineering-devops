#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]

    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(userId)).json()

    tasksList = []
    for task in todos:
        mydict = {}
        mydict["task"] = task.get('title')
        mydict["completed"] = task.get('completed')
        mydict["username"] = name.get('username')
        tasksList.append(mydict)
    json_obj = {}
    json_obj[userId] = tasksList
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
