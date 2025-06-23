from .auth import get_auth_token
from .extract import fetch_flight_data
from .transform import transform_flight_data
from .load import save_to_csv
from config.config import ORIGIN, DESTINATION, DEPARTURE_DATE

def run_etl():
    # max_results = 20
    token = get_auth_token()
    raw_data = fetch_flight_data(token, ORIGIN, DESTINATION, DEPARTURE_DATE)
    df = transform_flight_data(raw_data)
    print(df.head())
    save_to_csv(df)


if __name__ == "__main__":
    run_etl()
