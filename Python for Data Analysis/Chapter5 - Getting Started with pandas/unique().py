import pandas as pd
import numpy as np

obj = pd.Series(data=['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c']);
print(obj);

Array_of_the_unique_values_in_a_Series = obj.unique();
print(Array_of_the_unique_values_in_a_Series);