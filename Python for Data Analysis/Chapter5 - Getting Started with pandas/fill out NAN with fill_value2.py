import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.arange(12.).reshape((3, 4)), columns=['a', 'b', 'c', 'd']);
print(df);

df2 = pd.DataFrame(data=np.arange(20.).reshape((4, 5)), columns=['a', 'b', 'c', 'd', 'e']);
print(df2);

df2.loc[1, 'b'] = np.nan;
print(df2);

df = df.reindex(columns=df2.columns, fill_value=0);
print(df);