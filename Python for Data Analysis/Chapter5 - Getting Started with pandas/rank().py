import numpy as np
import pandas as pd

obj = pd.Series(data=[7, -5, 7, 4, 2, 0, 4], index=None);
print(obj);

ranked_obj = obj.rank();
print(ranked_obj);

obj2 = obj.rank(method="first");
print(obj2);

obj3 = obj.rank(ascending=False , method="max");
print(obj3);