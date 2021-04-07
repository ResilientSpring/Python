import numpy as np
import pandas as pd

format = lambda x: "%.2f" % x;

frame = pd.DataFrame(data=np.random.randn(4, 3),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"]);

print(frame);

result = frame.applymap(func=format);
print(result);

result2 = frame['e'].map(format);
print(result2);