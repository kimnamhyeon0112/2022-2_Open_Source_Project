import pandas as pd

df1 = pd.read_excel('./Week09/남북한발전전력량.xlsx', engine= 'openpyxl')
df2 = pd.read_excel('./Week09/남북한발전전력량.xlsx', engine= 'openpyxl', header=None)

print(df1)
print('\n')
print(df2)