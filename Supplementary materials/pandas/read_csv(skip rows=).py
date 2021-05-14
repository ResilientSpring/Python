# skiprows : Line numbers to skip while reading csv.
## If it’s an int then skip that lines from top
## If it’s a list of int then skip lines at those index positions
## If it’s a callable function then pass each index to this function to check if line to skipped or not.

# Reference: https://web.archive.org/web/20201231022908/https://thispointer.com/pandas-skip-rows-while-reading-csv-file-to-a-dataframe-using-read_csv-in-python/


import pandas as pd

usersDf = pd.read_csv(filepath_or_buffer="Realm.csv")
print(usersDf)

usersDf_skip_row = pd.read_csv(filepath_or_buffer="Realm.csv", skiprows=1)
print(usersDf_skip_row)
