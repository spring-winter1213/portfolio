import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import koreanize_matplotlib

# 1. 데이터 로드 및 전처리
df = pd.read_csv('depression_insomnia.csv')
df['진료년월_dt'] = pd.to_datetime(df['진료년월'], format='%Y년 %m월')
df = df.sort_values('진료년월_dt')

# 2. 선형 추세(Trend) 계산
# 시간을 숫자로 변환 (0, 1, 2, ...)
df['time_index'] = np.arange(len(df))
X = df[['time_index']]
y = df['우울증_환자수']

# 선형 회귀 모델 학습
model = LinearRegression()
model.fit(X, y)
df['trend'] = model.predict(X)

# 추세가 제거된 데이터 (실제값 - 추세값)
df['detrended_depression'] = df['우울증_환자수'] - df['trend']

# 3. 상관계수 재계산
corr_raw, _ = stats.pearsonr(df['대구_열대야일수'], df['우울증_환자수'])
corr_detrended, p_val = stats.pearsonr(df['대구_열대야일수'], df['detrended_depression'])

# --- 시각화: 추세 제거 과정 및 결과 ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# [상단 그래프] 원본 데이터와 추세선
ax1.plot(df['진료년월_dt'], df['우울증_환자수'], label='원본 데이터', color='royalblue', alpha=0.6)
ax1.plot(df['진료년월_dt'], df['trend'], label='장기 선형 추세', color='red', linestyle='--')
ax1.set_title('우울증 환자 수: 원본 데이터 vs 장기 추세선', fontsize=14)
ax1.legend()

# [하단 그래프] 추세 제거 후 열대야와의 비교 (이중 축)
ax2_heat = ax2
ax2_heat.bar(df['진료년월_dt'], df['대구_열대야일수'], color='orange', alpha=0.3, label='열대야 일수')
ax2_heat.set_ylabel('열대야 일수 (일)', color='orange')

ax2_dep = ax2.twinx()
ax2_dep.plot(df['진료년월_dt'], df['detrended_depression'], color='green', marker='o', markersize=4, label='추세 제거된 우울증 수')
ax2_dep.set_ylabel('우울증 변동 (추세 제외)', color='green')

plt.title(f'추세 제거 후 분석: 열대야 vs 우울증 변동 (상관계수: {corr_detrended:.3f})', fontsize=14)
fig.tight_layout()
plt.savefig('장기추세')
plt.show()

print(f"원본 데이터 상관계수: {corr_raw:.4f}")
print(f"추세 제거 후 상관계수: {corr_detrended:.4f}")
print(f"유의수준 (p-value): {p_val:.4f}")