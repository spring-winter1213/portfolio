import pandas as pd

# 1. 파일 읽기 (헤더 2줄 처리)
df = pd.read_excel('data/insumnia_daegu_202001_202508.xlsx')

# print(df)


daegu_row = df[df.iloc[:,0]=='대구']


daegu_row.to_csv('capture_daegu.csv', encoding='utf-8-sig')