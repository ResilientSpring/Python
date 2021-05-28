from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

dataset = fetch_california_housing(as_frame=True)

print(dataset)
