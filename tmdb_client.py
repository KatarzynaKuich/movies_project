import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODMxNzEyZThlYzgxNjgyYmEzYzUxNTI4YjkzODM5YiIsInN1YiI6IjYxYmI1YzU5ZDJmNWI1MDA0MWIyN2UzZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Kx8tFNbKwoydxINBmAL3xS4ARvG3J9Lo_GfpwTulakA"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, current_list):
    try:
        data = get_movies_list(current_list)
    except:
        data = get_movies_list("popular")

    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def search(search_query):
   base_url = "https://api.themoviedb.org/3/"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   endpoint = f"{base_url}search/movie/?query={search_query}"

   response = requests.get(endpoint, headers=headers)
   response = response.json()
   return response['results']