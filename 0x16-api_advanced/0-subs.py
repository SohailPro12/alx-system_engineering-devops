#!/usr/bin/python3
"""
queries the Reddit API
returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    data = response.json()

    return data['data']['subscribers']
