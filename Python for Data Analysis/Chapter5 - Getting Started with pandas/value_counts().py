import pandas as pd
import numpy as np

obj = pd.Series(data=['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c']);
print(obj);

value_frequency = obj.value_counts();
print(value_frequency);

value_frequency2 = pd.value_counts(obj.values, sort=False);
print(value_frequency2);