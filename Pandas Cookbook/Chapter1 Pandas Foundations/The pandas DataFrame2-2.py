import pandas as pd
import numpy as np
import io
import requests

url = "https://raw.githubusercontent.com/PacktPublishing/Pandas-Cookbook/master/data/movie.csv";
movies = pd.read_csv(url, usecols=[0, 1, 2]);
columns = movies.column;
index = movies.index;
data = movies.to_numpy();
print(data);