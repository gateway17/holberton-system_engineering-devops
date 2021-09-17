#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""
from urllib import request
import json
from sys import argv
import csv

# Who is the target?
TARGET_ID = argv[1]
# Storage in csv format
rows = []
row = []
FILE_NAME = '{}.csv'.format(TARGET_ID)
# PATHs that we need to make requests to
PATHS = {
 'Personal_D': "https://jsonplaceholder.typicode.com/users/{}"
 .format(TARGET_ID),
 'Personal_tasks': 'https://jsonplaceholder.typicode.com/todos/'
 }
# Variables we will need
tasks = []  # List of tasks Done by the TARGET
completed_tasks = 0  # Mount of completed tasks
total_tasks = 0  # Total tasks
# Make a GET request to get personal information about target
with request.urlopen(PATHS['Personal_D']) as buffer:
    """Make a GET request to get personal information about target"""
    data = buffer.read().decode('utf-8')
    data = json.loads(data)
    E_name = data['username']
# Get the whole list of tasks
with request.urlopen(PATHS['Personal_tasks']) as buffer:
    """Get the whole list of tasks"""
    data = buffer.read().decode('utf-8')
    data = json.loads(data)

TARGET_ID = int(TARGET_ID)
# Now, find how many of those tasks are for TARGET
for i in data:
    if i['userId'] == TARGET_ID:
        if i['completed']:
            completed_tasks += 1
            total_tasks += 1
            tasks.append(i['title'])
        else:
            total_tasks += 1

        row = i['userId'], E_name, i['completed'], i['title']
        rows.append(row)
    else:
        continue

with open(FILE_NAME, 'w') as buffer:
    csv_obj = csv.writer(buffer, delimiter=' ', quoting=csv.QUOTE_ALL)
    csv_obj.writerows(rows)
