import requestsapi as api
def auth(email: str, password: str) -> dict:
    """
    Get the authorization information for the final surge account

    :param email: The email you use to login
    :param password: Your password to Final Surge

    :returns login information:
    """
    payload = {"email" : email, "password" : password}
    response = api.POST("https://beta.finalsurge.com/api/login", headers=api.APPLICATION_JSON, json=payload)
    return response.json()
