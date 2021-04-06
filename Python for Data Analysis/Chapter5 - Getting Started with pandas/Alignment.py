import numpy as np
import pandas as pd

df1 = pd.DataFrame(data=np.arange(9.).reshape((3, 3)),
                   columns=list("bcd"), index=["Ohio", "Texas", "Colorado"]);

print(df1);

df2 = pd.DataFrame(data=np.arange(12.).reshape((4, 3)),
                   columns=list("bde"),
                   index=["Utah", "Ohio", "Texas", "Oregon"]);

print(df2);

df3 = df1 + df2;
print(df3);