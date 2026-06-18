# 🥜 Computer Vision 기반 헤이즐넛 이상 탐지

**기간:** 2025.XX ~ 2025.XX  
**인원:** 개인 프로젝트

---

> **📁 이미지 파일 위치 (노트북 실행 후 생성됨)**
>
> 모든 이미지는 노트북(`장윤진_project.ipynb`)을 처음부터 순서대로 실행하면 같은 폴더에 자동 저장됩니다.
>
> | 파일명 | 포트폴리오 삽입 위치 |
> |---|---|
> | `train_good.png` | 4. 데이터셋 — 정상 샘플 예시 |
> | `hsv_histogram.png` | 5-1. HSV Color Histogram 예시 |
> | `anomaly_score.png` | 5-2. Score Distribution 그래프 |
> | `threshold_search.png` | 5-3. Threshold 실험 결과 그래프 |
> | `test_image.png` | 5-4. 차영상 / 마스크 / Bounding Box |
> | `average.png` | 5-3. 결함 유형별 평균 점수 (추가 참고용) |
> | `crack.png` | 1. 프로젝트 개요 — 대표 이미지 |
> | `matrix_graph.png` | 6. 성능 평가 — Confusion Matrix |

---

# 1. 프로젝트 개요

![헤이즐넛 정상/불량 샘플 이미지](crack.png)

> 헤이즐넛 정상/불량 샘플 이미지

## 프로젝트 배경

제조 현장에서는 불량 데이터를 충분히 확보하기 어려운 경우가 많다.

본 프로젝트에서는 MVTec AD의 Hazelnut 데이터를 활용하여 정상 데이터만 학습한 뒤 이상 여부를 탐지하는 OCC(One-Class Classification) 기반 이상 탐지 시스템을 구현하였다.

또한 단순히 정상/이상을 판별하는 것을 넘어 이미지 내 이상 후보 영역을 시각화하는 후처리 기법도 함께 실험하였다.

---

# 2. 프로젝트 목표

- 정상 데이터만 이용한 이상 탐지 모델 구현
- HSV Color Histogram 기반 특징 추출
- Isolation Forest 기반 이상 탐지
- Threshold 최적화
- 이상 후보 영역 시각화

---

# 3. 사용 기술

| 구분 | 기술 |
|---|---|
| Language | Python |
| Library | OpenCV, NumPy, Pandas |
| ML | Scikit-Learn |
| Visualization | Matplotlib |
| Model | Isolation Forest |

---

# 4. 데이터셋

## MVTec AD - Hazelnut

![정상(Good) 샘플 이미지](train_good.png)

> 정상(Good) / Crack / Cut / Hole / Print

### 정상 데이터

- Good

### 불량 데이터

- Crack
- Cut
- Hole
- Print

---

# 5. 프로젝트 진행 과정

## 5-1. HSV Color Histogram 기반 특징 추출

### 문제

RGB는 조명 변화에 민감하여 색상 특징을 안정적으로 표현하기 어려웠다.

### 해결

HSV 공간으로 변환 후 Histogram을 생성하여 특징 벡터로 사용하였다.

### 구현 내용

- RGB → HSV 변환
- H, S, V 채널 Histogram 계산
- Histogram 정규화
- Feature Vector 생성

![HSV Color Histogram Feature Extraction](hsv_histogram.png)

### 결과

Print와 같은 색상 기반 결함 탐지에는 효과적이었다.

---

## 5-2. Isolation Forest 기반 이상 탐지

### 문제

불량 데이터 수가 적기 때문에 일반적인 지도학습 적용이 어려웠다.

### 해결

정상 데이터만 학습하는 One-Class Classification 방식을 적용하였다.

### 구현 내용

- 정상 데이터 학습
- Isolation Forest 모델 생성
- Anomaly Score 계산

### 결과

정상과 불량을 효과적으로 구분할 수 있었다.

![Score Distribution 그래프](anomaly_score.png)

---

## 5-3. Threshold 최적화

### 문제

Threshold 값에 따라 오탐(False Positive)과 미탐(False Negative)이 크게 달라졌다.

### 해결

다양한 Threshold를 실험하며 최적값을 탐색하였다.

### 구현 내용

- Threshold Grid Search
- Precision
- Recall
- F1 Score 비교

![Threshold 실험 결과 그래프](threshold_search.png)

### 결과

단순 기본값보다 더 안정적인 성능 확보

---

## 5-4. 차영상 기반 이상 후보 영역 시각화

### 문제

모델이 이상이라고 판단했더라도 사용자는 어느 위치를 이상으로 판단했는지 확인하기 어려웠다.

### 해결

정상 참조 이미지와 테스트 이미지의 차이를 이용하여 이상 후보 영역을 시각화하였다.

### 구현 내용

#### 1) Difference Image 생성

정상 이미지와 테스트 이미지의 픽셀 차이를 계산하였다.

```python
diff_gray = cv2.absdiff(ref_gray, test_gray)
```

#### 2) Threshold 적용

차이가 큰 영역만 남기도록 이진화하였다.

```python
_, binary = cv2.threshold(
    diff_gray,
    diff_thresh,
    255,
    cv2.THRESH_BINARY
)
```

#### 3) Morphology 연산

노이즈 제거를 위해 OpenCV Morphology를 적용하였다.

```python
cv2.morphologyEx(...)
```

#### 4) Contour Detection

이상 후보 영역을 추출하였다.

```python
cv2.findContours(...)
```

#### 5) Bounding Box 시각화

추출된 영역에 빨간 박스를 표시하였다.

```python
cv2.rectangle(...)
```

---

### 시각화 결과

![차영상 / 마스크 / Bounding Box 시각화](test_image.png)

> 좌상: 테스트 이미지 | 우상: Difference Image | 좌하: Binary Mask | 우하: 이상 후보 영역 Bounding Box

---

### 결과

Print와 같이 밝기 변화가 큰 결함은 비교적 명확하게 표시할 수 있었다.

반면 Crack, Cut과 같은 미세 결함은 헤이즐넛의 위치 변화와 표면 질감의 영향을 받아 정확한 위치 표시가 어려웠다.

이를 통해 전통적인 차영상 기반 시각화 기법의 가능성과 한계를 확인할 수 있었다.

---

# 6. 성능 평가

![Confusion Matrix](matrix_graph.png)

### 주요 결과

- 정상/불량 분류 가능
- Print 결함 탐지 우수
- Crack, Cut 탐지 한계 확인
- Color Histogram 특징의 장단점 분석

---

# 7. 배운 점

### 1. 모델보다 데이터가 중요하다

처음에는 모델을 바꾸면 성능이 향상될 것이라고 생각했다.

하지만 실제로는 데이터 특성과 결함 특성을 이해하는 과정이 훨씬 중요하다는 사실을 배웠다.

---

### 2. 특징 추출 방식의 한계를 경험했다

HSV Histogram은 색상 변화에는 강했지만 구조적 결함에는 한계가 있었다.

이를 통해 Feature Engineering의 중요성을 이해할 수 있었다.

---

### 3. 결과 수치보다 실패 사례 분석이 중요하다

단순 Accuracy보다

- 어떤 결함이 탐지되는지
- 어떤 결함이 탐지되지 않는지

직접 확인하는 과정이 성능 개선에 더 중요하다는 점을 배웠다.

---

# 8. 핵심 성과

- HSV Histogram 기반 이상 탐지 구현
- Isolation Forest 적용
- Threshold 최적화 수행
- Difference Image 기반 이상 후보 영역 시각화 구현
- Crack / Cut / Print 결함 특성 비교 분석
- 특징 추출 방식의 한계 도출
- 데이터 기반 문제 분석 역량 강화
