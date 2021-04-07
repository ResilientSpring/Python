import numpy as np
import pandas as pd

series = pd.Series(data=np.arange(3), index=['b', 'e', 'f']);
print(series);

frame = pd.DataFrame(data=np.arange(12.).reshape((4, 3)), columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"]);
print(frame);

addition = frame + series;

print(addition);

series2 = frame['d'];
print(series2);

subtract = frame.sub(other=series2, axis="index");
print(subtract);