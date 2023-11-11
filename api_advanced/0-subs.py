#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if invalid.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_bot/1.0'}

    # Make the HTTP request to get subreddit information
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # Subreddit not found, return 0
        return 0
    else:
        # Other error, return 0
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The number of subscribers in the '{subreddit_name}' subreddit is: {subscribers_count}")
