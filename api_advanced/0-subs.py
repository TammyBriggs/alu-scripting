#!/usr/bin/python3
"""API for finding number of subscribers in sub-reddit in total"""
import requests


def num_of_subs(subreddits):
    """goes through reddit API to find subs in given subreddit"""

    url = "https://reddit.com/r/{}/hot.json".format(subreddits)
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0.0 (SIPHO WAS HERE MAN)"
    }

    # If given subreddit isnt real
    if subreddits is None or not isinstance(subreddits, str):
        return 0

    try:
        # var for not allowing API redirections...cause reddit does that
        response = requests.get(url, headers=headers, redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0

    # Error handling for any exceptions that can occur from request
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
