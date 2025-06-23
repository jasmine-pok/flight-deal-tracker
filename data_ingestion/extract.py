import requests



def fetch_flight_data(token, origin, destination, departure_date):

    # Search for flights
    url_flight_api = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers_flight_api = {"Authorization": f"Bearer {token}"}
    param_flight_api = {
        "originLocationCode" : origin,
        "destinationLocationCode": destination,
        "departureDate" : departure_date,
        "adults" : "1",
        # "max" : str(max_results)
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