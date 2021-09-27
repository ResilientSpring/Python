import pandas as pd

rainfall = pd.DataFrame(data=[[200.1, 400.3, 1000.5],
                              [100.2, 300.4, 1100.6]],
                        columns=["City1", "City2", "City3"])

print(rainfall)
