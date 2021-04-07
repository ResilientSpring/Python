import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.arange(8).reshape((2, 4)), columns=['d', 'a', 'b', 'c'],
                     index=["three", "one"]);

print(frame);

frame2 = frame.sort_index();
print(frame2);

# There is no sort_columns().
frame3 = frame.sort_index(axis=1);
print(frame3);

# frame4 = frame.sort_columns();
# print(frame4);