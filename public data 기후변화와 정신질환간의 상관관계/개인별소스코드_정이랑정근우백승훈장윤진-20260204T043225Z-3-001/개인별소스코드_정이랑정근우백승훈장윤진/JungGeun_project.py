import pandas as pd

# 1. 파일 읽기 (헤더 2줄 처리)
df = pd.read_excel('data/insumnia_daegu_202001_202508.xlsx')


# print(df)


new_cols = []
current_top = None

for col in df.columns: #일단 칼럼을 가져옴
    top = col[0]
    sub = col[1]

    if  "Unnamed" not in top: #Unnamed가 아니면 저장
        current_top = top

    final_top = current_top if current_top else "Meta"
    new_cols.append((final_top, sub))
    

df.columns = pd.MultiIndex.from_tuples(new_cols)

daegu_row = df[df.iloc[:, 0] == '대구']

if not daegu_row.empty:
    row = daegu_row.iloc[0]
    data = {}
    for col in df.columns:
        if '년' in str(col[0]) and '월' in str(col[0]) and col[1] == '환자수':
            data[col[0]] = row[col]

    df_clean = pd.DataFrame(list(data.items()), columns=['날짜', '환자수'])

    df_clean['환자수'] = df_clean['환자수'].astype(str).str.replace(',', '').astype(float)
    df_clean['날짜'] = pd.to_datetime(df_clean['날짜'], format='%Y %m')

    df_clean = df_clean.sort_values('날짜')
    print(df_clean.head())

    df_clean.to_csv('insomnia_daegu_clean.csv', index=False, encoding='utf-8-sig')