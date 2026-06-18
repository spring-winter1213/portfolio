import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from scipy import stats

# 1. 데이터 로드 및 전처리
df = pd.read_csv('depression_insomnia.csv')
df.columns = ['날짜', '우울증', '불면증', '열대야']
df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월')
df = df.sort_values('날짜')

# 2. 시차(Lag) 데이터 생성 및 상관계수 계산
lags = [0, 1, 2, 3] # 0~3개월 시차
correlations = []

for lag in lags:
    # 열대야 데이터를 lag만큼 뒤로 밀기 (shift)
    # 예: lag=1이면 8월의 열대야 데이터가 9월 행에 위치하게 됨
    shifted_heat = df['열대야'].shift(lag)
    
    # 결측치 제거 후 상관계수 계산
    valid_data = pd.DataFrame({'heat': shifted_heat, 'dep': df['우울증']}).dropna()
    corr, _ = stats.pearsonr(valid_data['heat'], valid_data['dep'])
    correlations.append(corr)

# 3. 결과 시각화
plt.figure(figsize=(10, 6))
colors = ['#ced4da', '#74c0fc', '#339af0', '#1c7ed6'] # 시차에 따른 색상 변화
bars = plt.bar([f'시차 {l}개월' for l in lags], correlations, color=colors)

# 수치 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.005,
             f'{height:.3f}', ha='center', va='bottom', fontweight='bold')

plt.title('열대야 발생 시차(Lag)에 따른 우울증 상관계수 변화', fontsize=15, pad=10)
plt.ylabel('피어슨 상관계수 (r)', fontsize=12)
plt.ylim(0, max(correlations) + 0.05) # 여유 공간 확보
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('발생시차')
plt.tight_layout()
plt.show()

# 상세 결과 출력
for l, c in zip(lags, correlations):
    print(f"열대야 데이터 {l}개월 시차 적용 시 상관계수: {c:.4f}")