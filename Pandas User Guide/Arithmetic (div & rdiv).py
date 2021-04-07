import numpy as np
import pandas as pd

df = pd.DataFrame(data={"angles": [0, 3, 4], "degree": [360, 180, 360]},
                  index=["circle", "triangle", "rectangle"]);

print(df);

# df / 10
df2 = df.div(other=10);
print(df2);

# 10 / div
df3 = df.rdiv(other=10);
print(df3);

df4 = df / 10 ;
print(df4);

df5 = 10 / df;
print(df5);

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.div.html#pandas.DataFrame.div