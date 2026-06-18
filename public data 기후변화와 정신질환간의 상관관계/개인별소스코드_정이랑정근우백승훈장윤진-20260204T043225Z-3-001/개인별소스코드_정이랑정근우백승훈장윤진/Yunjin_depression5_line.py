import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from scipy import stats
import matplotlib.dates as mdates

# 1. 데이터 불러오기
df = pd.read_csv('depression_insomnia.csv')

# 2. 컬럼명 설정 (사용자 데이터 구조에 맞춤)
df.columns = ['날짜(월)', '우울증 환자수', '불면증 환자수', '열대야 일수']

# 3. 날짜 데이터 전처리 (에러 해결 핵심)
# '2020년 05월' 형식을 인식하도록 format을 지정합니다.
df['날짜(월)'] = pd.to_datetime(df['날짜(월)'], format='%Y년 %m월')
# 날짜 순으로 정렬하여 그래프 꼬임 방지
df = df.sort_values('날짜(월)')

# --- [그래프 1] 이중 축 그래프 (추이 비교) ---
fig, ax1 = plt.subplots(figsize=(14, 7))


# --- [그래프 2 & 3] 산점도 및 회귀선 (상관관계 파악) ---
plt.figure(figsize=(10, 7))
# regplot은 산점도(Scatter)와 회귀선(Regression Line)을 동시에 그려줍니다.
sns.regplot(data=df, x='열대야 일수', y='우울증 환자수', 
            scatter_kws={'alpha':0.6, 's':80, 'color':'gray'}, 
            line_kws={'color':'red', 'lw':2})

# 피어슨 상관계수 및 p-value 계산
# 결측치가 있을 경우를 대비해 dropna 처리 후 계산
clean_df = df[['열대야 일수', '우울증 환자수']].dropna()
correlation, p_value = stats.pearsonr(clean_df['열대야 일수'], clean_df['우울증 환자수'])

plt.title(f'열대야 일수와 우울증 환자 수의 상관관계\n(Pearson $r$ = {correlation:.3f}, $p$-value = {p_value:.4f})', fontsize=15)
plt.xlabel('열대야 일수 (일)', fontsize=12)
plt.ylabel('우울증 환자 수 (명)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import matplotlib.dates as mdates

# 1. 데이터 불러오기 및 컬럼 설정
df = pd.read_csv('depression_insomnia.csv')
df.columns = ['날짜(월)', '우울증 환자수', '불면증 환자수', '열대야 일수']

# 2. 날짜 데이터 전처리 (format 주의: 데이터 실제 형식에 맞출 것)
df['날짜(월)'] = pd.to_datetime(df['날짜(월)'], format='%Y년 %m월')
df = df.sort_values('날짜(월)')

# 3. 시각화
plt.figure(figsize=(12, 6))

# 월별 실제 환자 수 (점과 얇은 선)
plt.plot(df['날짜(월)'], df['우울증 환자수'], marker='o', markersize=4, 
         linestyle='-', color='royalblue', alpha=0.6, label='월별 환자 수')

# 6개월 이동 평균선 (전체적인 추세 파악)
# 월별 변동(노이즈)을 제거하고 흐름을 보여줍니다.
df['이동평균'] = df['우울증 환자수'].rolling(window=6, center=True).mean()
plt.plot(df['날짜(월)'], df['이동평균'], color='crimson', linewidth=3, label='6개월 이동평균(추세)')

# x축 포맷 설정
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3)) # 3개월 간격
plt.xticks(rotation=270)

# 레이블 및 제목
plt.title('시간의 흐름에 따른 우울증 환자 수 추이 분석', fontsize=15, pad=10)
plt.xlabel('날짜', fontsize=12)
plt.ylabel('환자 수 (명)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('시간의 흐름에 따른 우울증 환자 수 추이 분석')
plt.tight_layout()
plt.show()