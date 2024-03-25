import os
import requests

def authenticate_user_with_firebase(email, password):
    """
    Authenticate the user using email and password with Firebase.

    return: The response from the Firebase API.
    """
    
    api_key = os.getenv('FIREBASE_API_KEY')
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()