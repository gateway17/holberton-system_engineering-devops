#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""

if __name__ == "__main__":

    from urllib import request
    import json
    from sys import argv

    # PATHs that we need to make requests to
    PATHS = {
        'Personal_D': "https://jsonplaceholder.typicode.com/users/",
        'Personal_tasks': 'https://jsonplaceholder.typicode.com/todos/'
    }
    # Variables we will need
    tasks = []  # List of tasks Done by the TARGET
    completed_tasks = 0  # Mount of completed tasks
    total_tasks = 0  # Total tasks
    # Temporal list to add to the final dict
    temp_list = []
    # List of TARGET's ID
    id_list = []
    # Dict to return to json
    final_dict = {}
    # Name of json file
    FILE_NAME = 'todo_all_employees.json'

    E_name = ''

    u_buffer_id = {}

    # Make a GET request to get personal information about target
    with request.urlopen(PATHS['Personal_D']) as buffer:
        """Make a GET request to get personal information about target"""
        U_data = buffer.read().decode('utf-8')
        U_data = json.loads(U_data)

    # Get the whole list of tasks
    with request.urlopen(PATHS['Personal_tasks']) as buffer:
        """Get the whole list of tasks"""
        data = buffer.read().decode('utf-8')
        data = json.loads(data)

    # Now, find how many of those tasks are for TARGET

    # get the whole list of users ID
    for i in data:

        if i['userId'] not in id_list:
            id_list.append(i['userId'])

    # Iterates in Users ID, over all tasks
    for e in id_list:
        temp_list = []
        for a in data:
            if a['userId'] == e:
 
                for i in U_data:
                    if i['id'] == e:

                        E_name = i['name']

                        a = {'username': E_name, 'task': a['title'],
                            'completed': a['completed']}
                    else:
                        continue
                temp_list.append(a)
        e = str(e)
        final_dict[e] = temp_list

    with open(FILE_NAME, 'w') as buffer:
        """ Become whole tashs in a json"""
        json.dump(final_dict, buffer)
