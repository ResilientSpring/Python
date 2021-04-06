import numpy as np
import pandas as pd

data = pd.DataFrame(data=np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"]);

print(data);

data2 = data.drop(axis=1, labels=["two"]);
print(data2);