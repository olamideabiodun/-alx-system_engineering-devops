#!/usr/bin/python3
"""returns number of subreddit subscribers"""

import requests


def number_of_subscribers(subreddit):
    """gets number of subscribers to a certain reddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent':
               'script:subs1.0 by /u/faruqolamide'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
