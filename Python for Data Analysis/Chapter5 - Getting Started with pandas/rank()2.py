import numpy as np
import pandas as pd

frame = pd.DataFrame(data={'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]});
print(frame);

ranked_frame = frame.rank(axis="columns");
print(ranked_frame);