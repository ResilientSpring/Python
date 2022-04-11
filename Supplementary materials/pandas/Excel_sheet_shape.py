import pandas as pd

df = pd.read_csv("trace.txt", delimiter="\t")

print(df.shape)

# Reference:
# 1. https://stackoverflow.com/a/51067912/
# 2. https://www.adamsmith.haus/python/answers/how-to-find-the-total-number-of-rows-and-columns-of-an-excel-spreadsheet-in-python
# 3. https://www.google.com/search?q=find+total+number+of+columns+in+excel+with+python
