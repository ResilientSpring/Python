import pandas as pd

url = 'https://github.com/fzumstein/python-for-excel/blob/1st-edition/xl/course_participants.xlsx?raw=true'
df = pd.read_excel(url)
print(df)

# Search for the people who live in the USA and are older than 40 years.
condition = (df['age'] > 40) & (df['country'] == 'USA')
print(condition)

tf2 = df[condition]
print(tf2)

print(30*'=')

## Alternative
df3 = df.loc[condition, :]
print(df3)

print(30*'=')

# Search for the people who live in Europe and are older than 10 years.
condition = (df['age'] > 10) & (df['continent'] == 'Europe')
tf3 = df[condition]
print(tf3)

print(30*'=')

print(df.iloc[3, 1], df.iloc[2, 1])

print(30*'=')

df2 = pd.read_excel(url, index_col='user_id')
print(df2)

print(df2.loc[1003, 'name'])

print(30*'=')

# To filter the index, you can refer to it as df.index
condition = df2.index > 1001
over_thousand = df2[condition]
print(over_thousand)

# Search for the people who live in Italy or Germany
condition = (df2['country'] == 'Italy') | (df2['country'] == 'Germany')
print(condition)
result = df2[condition]
print(result)

condition = df2['country'] == ('Italy' and 'Germany')
resulting = df2[condition]
print(resulting)

# This could be the yearly rainfall in millimeters
rainfall = pd.DataFrame(data={'City 1': [300.1, 100.2],
                              'City 2': [400.3, 300.4],
                              'City 3': [1000.5, 1100.6]})

print(rainfall)

condition = rainfall < 400
print(condition)

selected_rainfall = rainfall[condition]
print(selected_rainfall)
