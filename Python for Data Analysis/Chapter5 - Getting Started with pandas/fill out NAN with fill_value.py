import numpy as np
import pandas as pd

df1 = pd.DataFrame(data=np.arange(12.).reshape((3, 4)), columns=list("abcd"));
print(df1);

df2 = pd.DataFrame(data=np.arange(20.).reshape((4, 5)), columns=list("abcde"));
print(df2);

df2.loc[1, 'b'] = np.nan;

print(df2);

df3 = df1 + df2;
print(df3);

df4 = df1.add(df2, fill_value=0);
print(df4);