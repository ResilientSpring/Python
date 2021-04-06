import numpy as np
import pandas as pd

df = pd.DataFrame(data={"one": [1., 2., 3.]});
print(df);

df.two = [4, 5, 6];
print(df);

df["three"] = [7, 8, 9];
print(df);