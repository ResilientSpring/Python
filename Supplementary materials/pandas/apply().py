import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3),
                     columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(frame)

def f(x):
    return x.max() - x.min()


frame.apply(f)

print(frame)

# Reference:
# 1. https://stackoverflow.com/a/19798528/14900011
