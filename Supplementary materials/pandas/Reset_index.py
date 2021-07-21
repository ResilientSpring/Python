import pandas as pd
import numpy as np

dataset = np.array([['day_time', 'data'],
                    ['2014-02-02', 0.45],
                    ['2014-02-02', 0.41]])

df = pd.DataFrame(data=dataset)

print(df)

df = df.set_index('day_time')
print(df)

settings = {'day_time': ['2014-02-02', '2014-02-02'], 'data': [0.45, 0.41]}
print(settings)
