import numpy as np
import pandas as pd

year = [2000, 2001, 2002];

dictionary = {2000: [None, 1.5], 2001: [2.4, 1.7], 2002: [2.9, 3.6]};

series = pd.Series(data=dictionary);
print(series);

# frame = pd.DataFrame(data=dictionary, columns=["Nevada", "Ohio"]);

# frame = pd.DataFrame(data=series, columns=["Nevada", "Ohio"]);

frame = pd.DataFrame(data=series);
print(frame);

frame2 = pd.DataFrame(data=dictionary);
print(frame2);

frame3 = frame2.T;
print(frame3);

frame3.columns = ["Nevada", "Ohio"];
print(frame3);

frame3.columns.name = "state";
frame3.index.name = "year";
print(frame3);

print(frame3.columns);

print("Ohio" in frame3.columns);
print(2003 in frame3.index);