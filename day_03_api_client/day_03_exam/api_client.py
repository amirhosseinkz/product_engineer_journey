import requests

from errors import ApiInvalidResponseError, ApiStatusError, ApiTimeoutError



def fetch_posts():


    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url ,timeout= 5)
    except requests.exceptions.Timeout as exc:
        raise ApiTimeoutError("The request timed out") from exc
    except requests.exceptions.RequestException as exc:
        raise ApiStatusError(f"An error occurred while making the request: {exc}") from exc
    
    if response.status_code != 200:
        raise ApiStatusError(f"Unexpected status code: {response.status_code}")
    
    try:
        data = response.json()
    except ValueError as exc:
        raise ApiInvalidResponseError("Failed to parse JSON response") from exc
    
    if not isinstance(data, list):
        raise ApiInvalidResponseError("Expected a list of posts in the response")
    
    return data

def fetch_post_by_id(post_id):

    if post_id <= 0:

        raise ValueError("Post ID must be greater than 0.")


    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url ,timeout= 5)
    except requests.exceptions.Timeout as exc:
        raise ApiTimeoutError("The request timed out") from exc
    except requests.exceptions.RequestException as exc:
        raise ApiStatusError(f"An error occurred while making the request: {exc}") from exc
    
    if response.status_code == 404:
        raise ApiStatusError(f"Post with ID {post_id} not found")
    
    if response.status_code != 200:
        raise ApiStatusError(f"Unexpected status code: {response.status_code}")
    
    try:
        data = response.json()
    except ValueError as exc:
        raise ApiInvalidResponseError("Failed to parse JSON response") from exc
    
    if not isinstance(data , dict):
       raise ApiInvalidResponseError("Expected a post object in the response.")
    return data


    
