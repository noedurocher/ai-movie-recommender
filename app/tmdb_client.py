import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []
    data = response.json()

    movies=[]
    for movie in data["results"]:
        movies.append({
            "title": movie["title"],
            "overview": movie["overview"]
        })
    return movies
