from dotenv import load_dotenv
import os

load_dotenv()

ORIGIN = os.getenv("ORIGIN")
DESTINATION = os.getenv("DESTINATION")
DEPARTURE_DATE = os.getenv("DEPARTURE_DATE")
