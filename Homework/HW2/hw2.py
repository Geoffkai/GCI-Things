import numpy as np
import pandas as pd
from pandas import DataFrame

# Libraries for retrieving data from the web and handling zip files
import requests, zipfile
from io import StringIO
import io

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# Load and clean the data
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_data_extracted = anime_data[anime_data['Score'] != 'Unknown'].copy()
anime_data_extracted['Score'] = pd.to_numeric(anime_data_extracted['Score'])

def homework(anime_data_extracted):
    result = anime_data_extracted.groupby("Type")['Score'].mean().sort_values(ascending=False)
    return result

your_answer = homework(anime_data_extracted)
print(your_answer)

case_2_data = pd.DataFrame({
    "Type": ["TV", "TV", "Movie", "Movie", "OVA"],
    "Score": [8.0, 6.0, 9.0, 7.0, 5.0],
})
case_2_answer = homework(case_2_data)
print(case_2_answer)