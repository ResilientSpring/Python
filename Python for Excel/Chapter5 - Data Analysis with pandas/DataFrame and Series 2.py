import pandas as pd

url = "https://github.com/fzumstein/python-for-excel/blob/9fedbd4ac0bcace2ddd49d73a41d2143d0768c19/xl/course_participants.xlsx?raw=true";
df = pd.read_excel(url, sheet_name="Sheet1");
print(df);

# Reference:
# https://stackoverflow.com/a/62194647/14900011