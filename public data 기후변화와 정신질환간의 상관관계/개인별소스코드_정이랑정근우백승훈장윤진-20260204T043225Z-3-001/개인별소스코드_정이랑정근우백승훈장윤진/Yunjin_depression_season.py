import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from scipy import stats
import matplotlib.dates as mdates

# 1. 데이터 로드 및 전처리
df = pd.read_csv('depression_insomnia.csv')

# 날짜 형식 변환 (2020년 05월 -> datetime 객체)
df['진료년월_dt'] = pd.to_datetime(df['진료년월'], format='%Y년 %m월')
df = df.sort_values('진료년월_dt')

# 분석을 위한 영문 컬럼명 매핑 (코드 작성 편의용)
df_eng = df.rename(columns={
    '우울증_환자수': 'depression',
    '불면증_환자수': 'insomnia',
    '대구_열대야일수': 'tropical_nights'
})

# 시각화 스타일 설정
sns.set_theme(style="whitegrid", font="NanumGothic") # 환경에 따라 폰트 설정 확인 필요

# --- [그래프 4] 월별 평균 계절성 패턴 ---
df['월'] = df['진료년월_dt'].dt.month
monthly_avg = df.groupby('월')[['우울증_환자수', '대구_열대야일수']].mean().reset_index()

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(monthly_avg['월'], monthly_avg['대구_열대야일수'], color='orange', alpha=0.6, label='평균 열대야')
ax1.set_ylabel('평균 열대야 일수')
ax1.set_xlabel('월')

ax2 = ax1.twinx()
ax2.plot(monthly_avg['월'], monthly_avg['우울증_환자수'], color='blue', marker='D', label='평균 환자 수')
ax2.set_ylabel('평균 우울증 환자 수')
plt.title('월별 평균 열대야 및 우울증 환자 수 (계절성)')
plt.xticks(range(1, 13))
plt.savefig('월별 평균 열대야 및 우울승 환자수')

plt.show()
