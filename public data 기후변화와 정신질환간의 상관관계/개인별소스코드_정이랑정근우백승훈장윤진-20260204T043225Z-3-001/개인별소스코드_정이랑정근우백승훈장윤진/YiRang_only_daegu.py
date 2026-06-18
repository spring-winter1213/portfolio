import pandas as pd

# 1) CSV 읽기
df = pd.read_csv("merged_heatwave_day.csv")

# 2) '지점' 컬럼에 '대구'가 들어있는 행만 필터링
daegu = df[df["지점"].astype(str).str.contains("대구", na=False)]

# 3) CSV로 저장 
daegu.to_csv("merged_heatwave_day_daegu.csv", index=False, encoding="utf-8-sig")

print("저장 완료:", len(daegu), "행")
