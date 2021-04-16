import pandas as pd
import numpy as np

url = "https://github.com/PacktPublishing/Machine-Learning-for-Finance/blob/master/1%20Excel%20Exercise.xlsx?raw=true";
df = pd.read_excel(io=url, sheet_name=0, header=1, index_col=None, usecols="A:N", nrows=180);
print(df);

y = df.iloc[:, 0];
print(y);