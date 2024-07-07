import json
import requests as requests

def fetch_ApiKey():
    with open('config/config.json', 'r') as f:
        data = json.load(f)
        return data['imdbApikey']

def search_movie_api(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"

    auth = f"Bearer {fetch_ApiKey()}"
    headers = {
        "accept": "application/json",
        "Authorization": auth
    }

    try:
        response = requests.get(url, headers=headers)
        search_results = response.json()
        return search_results["results"]
    except Exception as e:
        return f"An error occurred: {e}", 500


def get_movie_info(movie_title):
    movie_data = search_movie_api(movie_title)

    if len(movie_data) == 0:
        return False, []  # No movies found

    # Extracting specific keys from each dictionary in the JSON response
    desired_keys = ['backdrop_path', 'original_title', 'overview', 'release_date', 'title']
    filtered_response = [{key: movie.get(key, '') for key in desired_keys} for movie in movie_data]

    return True, filtered_response  # Movies found and their details
