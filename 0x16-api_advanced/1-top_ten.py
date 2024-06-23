#!/usr/bin/python3
"""returns number of subreddit subscribers"""

import requests


def top_ten(subreddit):
    """gets number of subscribers to a certain reddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent':
               'script:subs/1.0 by /u/faruqolamide'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        if res.status_code == 200:
            post_titles = [item['data']['title']
                           for item in res.json()['data']['children']
                           if item['kind'] == 't3']
            for title in post_titles:
                print(title)
    else:
        print("None")
        return 0
