import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)  # Use the OAuth endpoint
    headers = {'User-Agent': 'MyApp v1.0 by u/Silver_Oil1466'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if the request fails
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        print(subscribers)
        return subscribers
    except requests.RequestException as e:
        print(e)
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit_name = input("Enter a subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print("Subscribers for r/{}: {}".format(subreddit_name, subscribers))

