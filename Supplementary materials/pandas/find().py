# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(data)

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# substring to be searched
sub ='a'