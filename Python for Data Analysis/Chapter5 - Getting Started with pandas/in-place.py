import numpy as np
import pandas as pd

obj = pd.DataFrame(data=np.arange(8, 16, 1).reshape((2, 4)), index=["Utah", "New York"],
                   columns=["one", "two", "three", "four"]);

print(obj);

obj.drop(labels="four", axis=1, inplace=True);
print(obj);