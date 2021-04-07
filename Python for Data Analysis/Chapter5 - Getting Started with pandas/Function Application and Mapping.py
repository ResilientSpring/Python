import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.random.randn(4, 3),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"]);
print(frame);

frame2 = np.abs(frame);
print(frame2);