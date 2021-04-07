import numpy as np
import pandas as pd

frame = pd.DataFrame(data=np.random.randn(4, 3),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"]);

print(frame);

f = lambda x: x.max() - x.min();

result = frame.apply(func=f, axis="index");
print(result);

result2 = frame.apply(func=f, axis="columns");
print(result2);