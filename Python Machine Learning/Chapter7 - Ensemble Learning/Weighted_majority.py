import numpy as np
import pandas as pd

np.argmax(np.bincount([0, 0, 1], weights=[0.2, 0.2, 0.6]))

df = pd.DataFrame(data=[[0.9, 0.1], [0.8, 0.2], [0.4, 0.6]],
                  index=["Classifier1", "Classifier2", "Classifier3"],
                  columns=["Class 1", "Class 2"])

print(df)

p = df.multiply(other=[0.2, 0.2, 0.6], axis=0)
print(p)

print(p.iloc[:, 0].sum())

s = pd.Series(data=[p.loc[:, "Class 1"].sum(), p.loc[:, "Class 2"].sum()])
s.name = "Probability"
print(s)

total = p.append(other=s)
print(total)
