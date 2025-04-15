import pandas as pd

df= pd.read_csv("/work/neo/python/pythonData/NewChickenResult.csv",encoding='utf-8')

df= df[~df['sido'].astype(str).str.isnumeric()]

df = df[~df['sido'].astype(str).str.contains('테스트')]



result = df.groupby(['sido','brand']).size().reset_index(name='count')

print(result)