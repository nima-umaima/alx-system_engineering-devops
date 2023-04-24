#!/usr/bin/python3
""" This script returns information about employee's TODO list progress
    for a given employee ID.
    API URL: https://jsonplaceholder.typicode.com/
    API endpoits: users/, todos
"""
from requests import get
from sys import argv


def list_tasks(employee_id=None):
    """ Returns information about employee's TODO list progress
        for a given employee ID.
    """
    try:
        employee_id = int(employee_id)
    except:
        return

    API_URL = "https://jsonplaceholder.typicode.com/"

    employee = get(API_URL + "users/{}".format(employee_id)).json()
    todos = get(API_URL + "todos?userId={}".format(employee_id)).json()

    name = employee.get("name")
    tasks_total = len(todos)
    tasks_done = 0
    tasks_titles = []

    for task in todos:
        if task.get("completed") is True:
            tasks_titles.append(task.get("title"))
            tasks_done += 1

    del todos, employee

    print("Employee {}".format(name), end=" ")
    print("is done with tasks({}/{}):".format(tasks_done, tasks_total))
    for task in tasks_titles:
        print('\t', task)


if __name__ == "__main__":
    list_tasks(argv[1])
