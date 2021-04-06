import numpy as np
import pandas as pd

data = pd.DataFrame(data=np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"]);

print(data);
print(data.iloc[2]);

data2 = data.loc["Colorado", ["two", "three"]];
print(data2);

data3 = data.iloc[2, [3, 0, 1]];
print(data3);

data4 = data.iloc[[1, 2], [3, 0, 1]];
print(data4);