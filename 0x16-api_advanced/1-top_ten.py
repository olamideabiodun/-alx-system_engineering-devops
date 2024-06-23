#!/usr/bin/python3
"""returns number of subreddit subscribers"""

import requests

def number_of_subscribers(subreddit):
    """gets number of subscribers to a certain reddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent':
               'script:subs/1.0 by /u/faruqolamide'}
    
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        if res.status_code == 200:
            titles = [item['data']['title']]
            for item in titles:
                
        return res.json()['data']['children'][i]['data']['title']
    else:
        return 0
