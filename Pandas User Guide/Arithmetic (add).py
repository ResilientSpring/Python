import numpy as np
import pandas as pd

# Get Addition of dataframe and other, element-wise (binary operator add).

# Equivalent to dataframe + other, but with support to substitute a fill_value
# for missing data in one of the inputs. With reverse version, radd.

df = pd.DataFrame(data={"angles": [0, 3, 4], "degrees": [360, 180, 360]},
                  index=["circle", "triangle", "rectangle"]);

print(df);

df2 = df + 1;
print(df2);

df3 = df.add(other=1);
print(df3);

# Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html