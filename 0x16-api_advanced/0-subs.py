import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent to avoid Too Many Requests errors
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == "__main__":
    subreddit_name = input("Enter a subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print(f"Number of subscribers in r/{subreddit_name}: {subscribers}")
