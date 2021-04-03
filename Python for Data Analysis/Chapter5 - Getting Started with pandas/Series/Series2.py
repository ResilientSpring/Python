import pandas as pd

obj2 = pd.Series(data=[4, 7, -5, 3], index=['d', 'b', 'a', 'c'], name="page 172 (input 15)");
print(obj2);

# You can use labels in the index when selecting single values or a set of values:
print(obj2['a']);

obj2['d'] = 6;
# print(obj2['c', 'a', 'd']);
print(obj2[['c', 'a', 'd']]);