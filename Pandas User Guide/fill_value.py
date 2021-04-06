import numpy as np
import pandas as pd

df = pd.DataFrame(data={"angles": [0, 3, 4], "degrees": [360, 180, 360]},
                  index=["circle", "triangle", "rectangle"]);

print(df);

other = pd.DataFrame(data={"angles": [0, 3, 4]}, index=["circle", "triangle", "rectangle"]);
print(other);

df2 = df * other;
print(df2);

df3 = df.mul(other=other, fill_value=0);
print(df3);

# Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html#pandas.DataFrame.mul