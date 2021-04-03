import pandas as pd

obj2 = pd.Series(data=[4, 7, -5, 3], index=['d', 'b', 'a', 'c'], name="page 172 (input 21)");
print(obj2);

print([obj2 > 0]);

print([obj2[obj2 > 0]]);