import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movies = pd.read_csv(r"https://raw.githubusercontent.com/PacktPublishing/Pandas-Cookbook/master/data/movie.csv");
print(movies.to_string());