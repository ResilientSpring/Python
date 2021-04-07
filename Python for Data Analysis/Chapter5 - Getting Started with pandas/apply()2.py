import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.random.randn(4, 3),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"]);

print(frame);

def f(x):
    return pd.Series(data=[x.min(), x.max()], index=["min", "max"]);

frame2 = frame.apply(func=f);
print(frame2);