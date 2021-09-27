import pandas as pd

rainfall = pd.DataFrame(data=[[300.1, 400.3, 1000.5],
                              [100.2, 300.4, 1100.6]],
                        columns=["City1", "City2", "City3"])

print(rainfall)

rainfall_plus = rainfall + 100

print(rainfall_plus)

more_rainfall = pd.DataFrame(data=[[100, 200],
                                   [300, 400]], index=[1, 2], columns=["City 1", "City 4"])

print(more_rainfall)

more_rainfall_plus = rainfall + more_rainfall

print(more_rainfall_plus)

summation = rainfall.loc[1, :] + rainfall
print(summation)

summation2 = rainfall.add(rainfall.loc[:, "City2"], axis=0)
print(summation2)
