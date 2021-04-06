import numpy as np
import pandas as pd

date = pd.date_range(start="2000-01-01", periods=8);
df = pd.DataFrame(data=np.random.randn(8, 4), index=date, columns=['A', 'B', 'C', 'D']);
print(df);

df['A'] = np.arange(len(df.index));
print(df);

# Create new columns
df['E'] = np.arange(len(df.index));

print(df);