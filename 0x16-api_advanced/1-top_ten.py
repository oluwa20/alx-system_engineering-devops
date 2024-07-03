#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
   url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

   
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

   
    param = {
        "limit": 10
    }


    response = requests.get(url, headers=headers, param=param,
                            allow_redirects=False)
