from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API")
NEWS_API_KEY = os.getenv("NEWS_API")