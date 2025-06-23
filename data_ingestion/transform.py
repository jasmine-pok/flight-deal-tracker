import pandas as pd
import re
from datetime import timedelta


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
    df["duration"] = df["duration"].apply(parse_duration)
    return df