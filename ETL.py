# This is a script written to extract data with OMDB API

import requests
import pandas as pd
from sqlalchemy import create_engine

def extract_data(api_key, movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

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

# print(transformed_data)

def load_data(df, db_url):
    engine = create_engine(db_url)
    df.to_sql('movies', engine, if_exists='append', index=False)

def etl_process(api_key, movie_title, db_url):
    # Extract movie data
    movie_data = extract_data(api_key, movie_title)
    # Transform movie data
    transformed_data = transform_data(movie_data)
    # Load movie data
    load_data(transformed_data, db_url)
    
# API key to use OMDB API
# You can get one here https://omdbapi.com/apikey.aspx
api_key = '[your_api_key]'
movie_titles = ['Iron Man', 'The Incredible Hulk', 'Thor', 'Doctor Strange', 'Deadpool', 'Black Panther']
db_url = 'postgresql+psycopg2://[your_username]:[your_password]@localhost/moviedb'

for movie_title in movie_titles:
    print(movie_title)
    etl_process(api_key, movie_title, db_url)
print('ETL Process complete')
