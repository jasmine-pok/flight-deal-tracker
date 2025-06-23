import requests
from dotenv import load_dotenv
import os

def get_auth_token():

    # load environment variables
    load_dotenv()
    amadeus_api_key = os.getenv('AMADEUS_CLIENT_ID')
    amadeus_secret_key = os.getenv('AMADEUS_CLIENT_SECRET')

    # authenticate with AMEDEUS
    url_auth =  "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers_auth = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    data_auth = {
            "grant_type": "client_credentials",
            "client_id": amadeus_api_key,
            "client_secret": amadeus_secret_key
        }
    
    auth_response = requests.post(
        url=url_auth, 
        headers=headers_auth,
        data=data_auth)
    
    # error handling
    if auth_response.status_code != 200:
        raise Exception(f"Auth failed: {auth_response.text}")

    # token = auth_response.json().get("access_token")
    """
    print(f"status code: {response.status_code}")
    print(f"json format: {response.json()}")
    print(f"token: {token}")
    """
    return auth_response.json()["access_token"]