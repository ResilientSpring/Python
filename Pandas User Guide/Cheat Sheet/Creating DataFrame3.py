import numpy as np
import pandas as pd

df = pd.DataFrame(
    data=
    [ [4, 5, 6],
      [7, 8, 9]
    ],

    columns=['a', 'b', 'c'],
    index=[1, 2,]
)

print(df);