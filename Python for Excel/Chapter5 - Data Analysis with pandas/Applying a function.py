import pandas as pd

rainfall = pd.DataFrame(data=[[300.1, 400.1, 1000.5],
                              [100.2, 300.4, 1100.6]],
                        columns=["City 1", "City 2", "City 3"])

print(rainfall)

def format_string(x):
    return f"{x:,.2f}"


# Note that we pass in the function without calling it.
rainfall.applymap(format_string)

print(rainfall)
