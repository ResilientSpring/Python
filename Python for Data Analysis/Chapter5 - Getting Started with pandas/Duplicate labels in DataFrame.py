import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randn(4, 3), index=['a', 'a', 'b', 'b']);
print(df);

print(df.loc['b']);