import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                     columns=["Ohio", "Texas", "California"]);

print(frame);

states = ["Texas", "Utah", "California"];

# The columns can be re-indexed with the columns keyword:
frame2 = frame.reindex(columns=states);

print(frame2);