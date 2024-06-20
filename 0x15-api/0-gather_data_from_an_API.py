#!/usr/bin/python3

"""imports urllib.request to use the request module,
    imports the json to jsonify the fetched data"""
import requests
import sys


if __name__ == "__main__":
    all_tasks = []
    numb = 0
    user_id = int(sys.argv[1])
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(user_id)).json()

    users = response.get("name", "username")

    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    for t in tasks:
        if t.get("userId") is user_id:
            all_tasks.append(t)
            if t.get("completed") is True:
                numb += 1
    print("Employee {} is done with tasks ({}/{}):".format(users, numb,
                                                           (len(all_tasks))))
    for t in all_tasks:
        if t.get("completed") is True:
            title = t.get("title")
            print(f"\t{title}")
