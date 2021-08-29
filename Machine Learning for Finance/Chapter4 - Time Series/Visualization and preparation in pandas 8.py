import pandas as pd

train = pd.read_csv('train_1.csv').fillna(0)
print(train.head())

def parse_page(page):
    x = page.split('_') # split the string by underscore.
    return ''.join(x[:-3]), x[-3], x[-2], x[-1]


print(parse_page(train.Page[0]))


l = list(train.Page.apply(parse_page))
df = pd.DataFrame(l)
df.columns = ['Subject', 'Sub_Page', 'Access', 'Agent']

train = pd.concat([train, df], axis=1)
del train['Page']
