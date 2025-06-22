import requests
from dotenv import load_dotenv
import os
import pandas as pd
import json
import datetime as dt
import re
from datetime import timedelta

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


def fetch_flight_data(token, origin, destination, departure_date, max_results):

    # Search for flights
    url_flight_api = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers_flight_api = {"Authorization": f"Bearer {token}"}
    param_flight_api = {
        "originLocationCode" : origin,
        "destinationLocationCode": destination,
        "departureDate" : departure_date,
        "adults" : "1",
        "max" : str(max_results)
    }

    flights_response = requests.get(
        url=url_flight_api,
        headers=headers_flight_api,
        params=param_flight_api
    )
    
    # error handling
    if flights_response.status_code != 200:
        print(f"Failed to fetch flights info: {flights_response.text}")

    # flights_response_json = flights_response.json()
    # print(flights_response_json)
    # print(json.dumps(flights_response.json(), indent=2))
    return flights_response.json()

def parse_duration(iso_duration):
        match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?", iso_duration)
        if match:
            hours = int(match.group(1)) if match.group(1) else 0
            minutes = int(match.group(2)) if match.group(2) else 0
            return timedelta(hours=hours, minutes=minutes)
        else:
            return None

def transform_flight_data(raw_data):

    rows = []

    for data in raw_data["data"]:
        segment = data["itineraries"][0]["segments"]
        row = {
            "airline": segment[0]["carrierCode"],
            "flight_id": segment[0]["number"],
            "origin": segment[0]["departure"]["iataCode"],
            "destination": segment[-1]["arrival"]["iataCode"],
            "departure": segment[0]["departure"]["at"],
            "arrival": segment[0]["arrival"]["at"],
            "duration": data["itineraries"][0]["duration"],
            "price": data["price"]["total"],
            "currency": data["price"]["currency"],
            "stops": len(segment) - 1,
            "checked_bags": data["pricingOptions"]["includedCheckedBagsOnly"]
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df["departure"] = pd.to_datetime(df["departure"])
    # df["departure"] = df["departure"].dt.strftime("%Y-%m-%d %H:%M")
    df["arrival"] = pd.to_datetime(df["arrival"])
    # df["arrival"] = df["arrival"].dt.strftime("%Y-%m-%d %H:%M")
    return df
    
def save_to_csv(df):
        departure_date = df["departure"].iloc[0].strftime("%Y-%m-%d")
        file_name = f"flight_deals_{departure_date}.csv"
        folder_path = "data/raw"

        # Create folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Build full path
        file_path = os.path.join(folder_path, file_name)

        # Save the DataFrame
        df.to_csv(file_path, index=False)
        print(f"Saved file to: {file_path}")



def main():
    origin = "HOU"
    destination = "MIA"
    departure_date = "2025-08-01"
    max_results = 10

    token = get_auth_token()
    raw_data = fetch_flight_data(token, origin, destination, departure_date, max_results)
    df = transform_flight_data(raw_data)
    print(df.head())
    save_to_csv(df)


if __name__ == "__main__":
    main()
