import numpy as np
import pandas as pd

one = {"year": 2000, "state": "Ohio", "pop": 1.5, "debt": None};
two = {"year": 2001, "state": "Ohio", "pop": 1.7, "debt": -1.2};
three = {"year": 2002, "state": "Ohio", "pop": 3.6, "debt": None};
four = {"year": 2001, "state": "Nevada", "pop": 2.4, "debt": -1.5};
five = {"year": 2002, "state": "Nevada", "pop": 2.9, "debt": -1.7};
six = {"year": 2003, "state": "Nevada", "pop": 3.2, "debt": None};

frame = pd.DataFrame(data=[one, two, three, four, five, six]);
print(frame);