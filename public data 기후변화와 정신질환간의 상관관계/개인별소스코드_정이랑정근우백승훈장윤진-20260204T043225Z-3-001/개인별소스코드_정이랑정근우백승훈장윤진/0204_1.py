import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
# 데이터 설정
labels = ['1926년', '2025년']
values = [6.7, 28.0]

plt.figure(figsize=(8, 7))


bars = plt.bar(labels, values, color=['lightgray', 'orangered'], width=0.5, label='열대야 일수 (bar)')


# 막대 그래프 위에 수치 추가 (6.7일, 28.0일)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{height}일', ha='center', fontweight='bold')


# 증가폭 화살표 및 텍스트 추가
plt.annotate('', xy=(1, 28.0), xytext=(0, 6.7), arrowprops=dict(facecolor='black', shrink=0.05))
plt.text(0.5, 18, '4.2배 증가', fontsize=14, color='red', fontweight='bold', ha='center')

plt.title("<대한민국 열대야 일수 100년간의 변화>", fontsize=15)
# 왼쪽 레전드 추가

plt.legend(loc='upper left')

plt.grid(axis='y', alpha=0.3)
plt.show()

# 주석: 각 막대 상단에 데이터 수치를 직접 기입하여 가독성을 높였습니다.

'''
그래프 데이터 해석 (Analysis)
비교의 극대화: 1926년(6.7일) 대비 2025년(28.0일)의 열대야 일수는 약 4.2배 폭증했습니다. 이는 단순히 '더워졌다'는 수준을 넘어, 우리의 밤이 생존을 위협받는 환경으로 변했음을 의미합니다.
시각적 임팩트: 회색(과거)과 오렌지색(현재)의 대비, 그리고 중앙의 화살표는 청중에게 "기후 위기가 남의 일이 아니다"라는 경각심을 줍니다.
수면의 질 하락: 28일이라는 수치는 한 달 내내 밤잠을 설친다는 뜻이며, 이는 곧 프로젝트의 본론인 불면증 및 우울증 환자 증가의 직접적인 원인 근거가 됩니다.
'''