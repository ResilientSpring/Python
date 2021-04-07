import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.arange(12.).reshape((4, 3)),
                     index=["Utah", "Ohio", "Texas", "Oregon"],
                     columns=list("bde"));

print(frame);

series = frame.iloc[0];
print(series);

subtraction = frame - series;
print(subtraction);