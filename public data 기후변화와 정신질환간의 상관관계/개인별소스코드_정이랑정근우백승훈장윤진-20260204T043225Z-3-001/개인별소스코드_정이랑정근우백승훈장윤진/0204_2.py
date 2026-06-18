import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
df = pd.read_csv('(100)OBS_ASOS_ANL_20260203154634.csv', encoding='cp949')

plt.figure(figsize=(12, 6))

# 1. 평균최고기온 라인 및 산점도

plt.plot(df['일시'], df['평균최고기온(°C)'], color='orangered', alpha=0.3)
plt.scatter(df['일시'], df['평균최고기온(°C)'], c=df['평균최고기온(°C)'], cmap='YlOrRd', s=30)


# 2. 추세선 (5년 이동 평균)
plt.plot(df['일시'], df['평균최고기온(°C)'].rolling(window=5).mean(), color='darkred', linewidth=3, label='5년 이동 평균(상승 추세)')

plt.title("<대구 평균 최고기온 상승 추이(1926 ~ 2025)>", fontsize=16, loc='center')
plt.axhline(df['평균최고기온(°C)'].mean(), color='gray', linestyle='--', label='전체 기간 평균')
plt.legend(loc='upper left')
plt.ylabel("평균 최고기온 (°C)")
plt.show()

# 주석: 낮 기온의 고점이 과거에 비해 눈에 띄게 높아지고 있으며, 최근으로 올수록 평균선 위로 데이터가 집중됩니다.

'''
평균 최고기온'의 정의와 시간
기상청 데이터에서 말하는 '평균 최고기온'은 특정 기간(일, 월, 년) 동안 매일 발생한 '최고기온'들의 평균값을 의미합니다.
측정 시간: 최고 기온은 보통 오후 2시에서 4시 사이에 관측됩니다. 하루 중 태양 복사 에너지가 지표면을 가장 많이 달군 시점의 온도입니다.
데이터의 성격: (100)OBS_ASOS_ANL... 파일은 대구의 1년 단위(연간) 통계 데이터입니다. 즉, 매년 1월 1일부터 12월 31일까지 365일 동안 발생한 모든 최고기온을 더해 365로 나눈 값입니다
'''