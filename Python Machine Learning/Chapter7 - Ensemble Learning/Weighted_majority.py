import numpy as np
import pandas as pd

np.argmax(np.bincount([0, 0, 1], weights=[0.2, 0.2, 0.6]))

df = pd.DataFrame(data=[[0.9, 0.1], [0.8, 0.2], [0.4, 0.6]])