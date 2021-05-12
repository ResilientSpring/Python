import pandas as pd

url = "https://github.com/fzumstein/python-for-excel/blob/1st-edition/xl/course_participants.xlsx?raw=true"

df = pd.read_excel(url, sheet_name="Sheet1")

print(df)

print(df.loc[2, "country"])


