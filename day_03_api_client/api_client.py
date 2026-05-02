import requests


from errors import ApiClientError, ApiInvalidResponseError, ApiStatusError, TimeoutError


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url , timeout= 10)
    except requests.exceptions.Timeout as exc:
        raise TimeoutError("The request timed out") from exc
    except requests.exceptions.RequestException as exc:
        raise ApiStatusError(f"An error occurred while making the request: {exc}") from exc
    
    if response.status_code != 200:
        raise ApiStatusError(f"Unexpected status code: {response.status_code}")
    
    try:
        data = response.json()
    except ValueError as exc:
        raise ApiInvalidResponseError("Failed to parse JSON response") from exc
    
    if not isinstance(data, list):
        raise ApiInvalidResponseError("Expected a list of users in the response")
    
    return data


def fetch_users_by_id(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url , timeout= 10)
    except requests.exceptions.Timeout as exc:
        raise TimeoutError("The request timed out") from exc
    except requests.exceptions.RequestException as exc:
        raise ApiStatusError(f"An error occurred while making the request: {exc}") from exc
    
    if response.status_code != 200:
        raise ApiStatusError(f"Unexpected status code: {response.status_code}")
    
    try:
        data = response.json()
        print(f"Data received for user ID {user_id}: {data}")
    except ValueError as exc:
        raise ApiInvalidResponseError("Failed to parse JSON response") from exc
    
    if not isinstance(data, dict):
        raise ApiInvalidResponseError("Expected a user object in the response")
    
    return data


