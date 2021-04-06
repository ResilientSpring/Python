import numpy as np
import pandas as pd

dates = pd.date_range(start="2000-01-01", periods=8);
df = pd.DataFrame(data=np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D']);
print(df);

dfa = df.copy();
print(dfa);

print(dfa.A);