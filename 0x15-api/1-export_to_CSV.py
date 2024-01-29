#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    userId = sys.argv[1]

    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(userId)).json()

    with open("{}.csv".format(userId), 'w') as acsvfile:
        csvwriter = csv.writer(acsvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csvwriter.writerow([userId, name.get('username'),
                                task.get('completed'), task.get('title')])
