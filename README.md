# Movie Data ETL Pipeline

## Project Overview

This project involves building an ETL (Extract, Transform, Load) pipeline that extracts movie data from the OMDB API, transforms it into a usable format, and loads it into a local PostgreSQL database. 
The project demonstrates the ability to handle real-world data processing tasks using Python and local development tools.

## Features

- Extract movie data from the OMDB API
- Transform the raw JSON data into a structured format using pandas
- Load the transformed data into a local PostgreSQL database
- Utilize Python and SQLAlchemy for data processing and database interaction
- Automated ETL process with a single script

## Requirements

- Python 3.x
- PostgreSQL
- pip (Python package installer)

### Python Libraries

- requests
- pandas
- sqlalchemy
- psycopg2-binary

## Setup Instructions

### 1. Install PostgreSQL

Download and install PostgreSQL from the [official website](https://www.postgresql.org/download/). Follow the installation instructions and set a password for the default `postgres` user.

### 2. Create a Database and User

Open the PostgreSQL shell (psql) or use a graphical interface like pgAdmin. Create a new database and user:
```
CREATE DATABASE moviedb;
CREATE USER your_username WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE moviedb TO your_username;
```

### 3. Clone the repository

Clone this repository to your local machine.
```
git clone https://github.com/vincentdiep/Movie-Data-ETL-Pipeline.git
cd Movie-Data-ETL-Pipeline
```

### 4. Install Python Dependencies

You can install the required Python libraries using pip:
```
pip install requests pandas sqlalchemy psycopg2-binary
```

### 5. Configure the Script

Open the 'ETL.py' file and replace the placeholders with your own PostgreSQL credentials and OMDB API key.
The placeholders should look like the following:
```
api_key = '[your_api_key]'
db_url = 'postgresql+psycopg2://[your_username]:[your_password]@localhost/moviedb'
```
Replace the brackets as well.

### 6. Run the ETL Pipeline

Run the script to execute the ETL pipeline.

```
python ETL.py
```

### Project Structure

- 'ETL.py': The main script that performs the ETL process.
- 'README.md': This README file.
- '.gitignore': Git ignore file to exclude unnecessary files from version control.

### Querying the Database using PostgreSQL Command Line Tool (psql)

1. In psql:
```
psql -U [your_username] -d moviedb
```

2. Run a SQL query:
    For example, let's look at all of the data from the movies table.
```
SELECT * FROM movies;
```
Results from the data I pulled:
![movie_query-etl](https://github.com/vincentdiep/Movie-Data-ETL-Pipeline/assets/51553736/c9776ebe-4499-4ba0-956d-bde4ab3850ad)
