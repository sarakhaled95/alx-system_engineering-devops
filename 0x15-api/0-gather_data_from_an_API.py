#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    userId = sys.argv[1]

    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(userId)).json()

    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".
          format(name.get("name"), len(completed), len(todos)))
    for complete in completed:
        print("\t {}".format(complete))
