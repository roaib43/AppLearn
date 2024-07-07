import requests as requests


def search_movie_api(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDQ5ZjA4NDJjYTQxYTNhZTk1N2YyNGMwNGFjMWE0NSIsIm5iZiI6MTcyMDMwODA0OS40MTMyODQsInN1YiI6IjY2NjYxOTAwOTY0ZTI5NzZhMmE2N2MwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yey2D1hBmGMBs08hbAVmHYq0YHx-u314A9lL946Bcss"
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
