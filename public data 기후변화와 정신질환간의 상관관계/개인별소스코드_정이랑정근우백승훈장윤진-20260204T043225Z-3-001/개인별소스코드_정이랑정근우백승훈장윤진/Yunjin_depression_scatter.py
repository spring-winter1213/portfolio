import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from scipy import stats

# 1. 데이터 불러오기 및 전처리
df = pd.read_csv('depression_insomnia.csv')
df.columns = ['날짜(월)', '우울증 환자수', '불면증 환자수', '열대야 일수']

# 2. 산점도 및 회귀선 시각화
plt.figure(figsize=(10, 7))

# sns.regplot은 산점도와 선형 회귀 직선을 함께 그려줍니다.
sns.regplot(data=df, x='열대야 일수', y='우울증 환자수', 
            scatter_kws={'alpha':0.6, 's':80, 'color': 'royalblue'}, 
            line_kws={'color':'red', 'label': '회귀선(Regression Line)'})

# 3. 상관계수 계산 (Pearson correlation)
# 결측치가 있다면 제거하고 계산합니다.
clean_df = df[['열대야 일수', '우울증 환자수']].dropna()
correlation, p_value = stats.pearsonr(clean_df['열대야 일수'], clean_df['우울증 환자수'])

# 그래프 제목 및 레이블 설정
plt.title(f'열대야 일수와 우울증 환자 수 산점도 분석)', 
          fontsize=14, pad=10)
plt.xlabel('열대야 일수 (일)', fontsize=12)
plt.ylabel('우울증 환자 수 (명)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.savefig('산점도')
plt.tight_layout()
plt.show()

print(f"상관분석 결과:")
print(f"- 피어슨 상관계수 ($r$): {correlation:.4f}")
print(f"- 유의수준 ($p$-value): {p_value:.4f}")