import requests

from Encoder import encoded_credentials

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data["access_token"]
    else:
        raise Exception("Couldn't get access token", response_data)