import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                     columns=["Ohio", "Texas", "California"]);

print(frame);

states = ["Texas", "Utah", "California"];

# frame2 = frame.loc[['a', 'b', 'c', 'd'], states];
# print(frame2);