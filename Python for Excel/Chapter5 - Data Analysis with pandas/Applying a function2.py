import pandas as pd

rainfall = pd.DataFrame(data=[[300.1, 400.1, 1000.5],
                              [100.2, 300.4, 1100.6]],
                        columns=["City 1", "City 2", "City 3"])

print(rainfall)

rainfall.applymap(lambda x: f"{x:,.2f}")

print(rainfall)
