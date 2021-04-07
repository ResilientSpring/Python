import numpy as np
import pandas as pd

frame = pd.DataFrame(data={'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]});
print(frame);

sort_column = frame.sort_values(by='b');
print(sort_column);

sort_multi_columns = frame.sort_values(by=['a', 'b']);
print(sort_multi_columns);