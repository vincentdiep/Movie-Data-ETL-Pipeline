# This is a script written to extract data with OMDB API
# This specific version was written by Vincent Diep for data on the movie 'Deadpool'

import requests
import pandas as pd

def extract_data(api_key, movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

api_key = '9be005ab'
movie_title = 'Deadpool'
movie_data = extract_data(api_key, movie_title)
# print(movie_data)

def transform_data(data):
    # Converting to DataFrame for easier transformation
    df = pd.DataFrame([data])
    # Selecting relevant columns
    df = df[['Title', 'Year', 'Genre', 'Director', 'Actors', 'imdbRating']]
    # Renaming columns for consistency
    df.columns = ['title', 'year', 'genre', 'director', 'actors', 'imdb_rating']
    # Converting data types if necessary
    df['year'] = df['year'].astype(int)
    df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
    return df

transformed_data = transform_data(movie_data)
print(transformed_data)