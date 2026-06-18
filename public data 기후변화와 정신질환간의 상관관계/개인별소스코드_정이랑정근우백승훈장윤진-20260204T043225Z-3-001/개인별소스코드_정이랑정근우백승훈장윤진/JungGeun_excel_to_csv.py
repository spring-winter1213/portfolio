import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df_raw = pd.read_excel('data/insumnia2020_01_2025_08.xlsx')

# print(tabulate(df, headers='keys', tablefmt='psql'))

# row = df.iloc[1] 나중에 '계'를 뽑기
# print(row)

# 일단 연도별 환자수를 뽑아야함.
df_raw.to_csv('data/insumnia2020_01_2025_08.csv', index=False, encoding='utf-8-sig')
