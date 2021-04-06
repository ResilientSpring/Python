import numpy as np
import pandas as pd

obj = pd.Series(data=np.arange(5.), index=['a', 'b', 'c', 'd', 'e']);
print(obj);

# Copy obj where its index is dropped/removed.
new_obj = obj.drop('c');

print(new_obj);

print(obj);

new_obj2 = obj.drop(labels=['d', 'c']);

print(new_obj2);