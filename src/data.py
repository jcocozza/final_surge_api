import requestsapi as api
import auth

def get_activities(user_token: str, scope_key: str, start_date: str, end_date: str) -> dict:
    """
    Get final surge activities in the range

    :param user_token: The user token returned from authorization
    :param scope_key: The scope key returned from authorization
    :param start_date: The start date of the interval, format: YYYY-MM-DD
    :param end_date: The end date of the interval, format: YYYY-MM-DD

    :returns a dictionary of activities:
    """
    headers = {
        "Authorization": f"Bearer {user_token}"
    }
    params = {
        "scope": "USER",
        "scopekey": f"{scope_key}",
        "startdate": f"{start_date}",
        "enddate": f"{end_date}"
    }
    response = api.GET("https://beta.finalsurge.com/api/WorkoutList", headers=headers, params=params)
    return response.json()

def main(username: str, password: str, start_date: str, end_date: str) -> dict:
    """
    :param email: The email you use to login
    :param password: Your password to Final Surge
    :param start_date: The start date of the interval, format: YYYY-MM-DD
    :param end_date: The end date of the interval, format: YYYY-MM-DD

    :returns a dictionary of activities:
    """
    info = auth.auth(username, password)
    token = info["data"]["token"]
    user_key = info["data"]["user_key"]

    activites = get_activities(token, user_key, start_date, end_date)
    return activites['data']
