import pandas as pd
import numpy as np
import io
import requests

url = "https://raw.githubusercontent.com/PacktPublishing/Pandas-Cookbook/blob/master/data/movie.csv";
s = requests.get(url).content;
movies = pd.read_csv(io.StringIO(s.decode("utf-8")));
columns = movies.column;
index = movies.index;
data = movies.to_numpy();
print(data);