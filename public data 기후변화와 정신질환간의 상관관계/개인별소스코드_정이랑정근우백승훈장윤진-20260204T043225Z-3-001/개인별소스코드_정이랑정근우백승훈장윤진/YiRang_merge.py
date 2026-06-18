#열대야관련 파일 병합 소스코드

import pandas as pd
import glob

files = sorted(glob.glob("data/ISSUE_HW_DAY_*.xls"))

dfs = []
for f in files:
    # 1) 탭( \t ) 구분 시도
    try:
        df = pd.read_csv(f, sep="\t", encoding="cp949")
    except Exception:
        # 2) 콤마 구분 시도
        df = pd.read_csv(f, encoding="cp949")
    dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)
merged.to_csv("merged_heatwave_day.csv", index=False, encoding="utf-8-sig")


