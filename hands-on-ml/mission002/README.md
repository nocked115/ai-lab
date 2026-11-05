# Mission 002 — California Housing Price Prediction

## 1. 프로젝트 개요

**목표:** California Housing 데이터셋을 활용해 주택 가격 예측 모델을 구축하고, 데이터 전처리부터 모델 학습, 교차 검증, 하이퍼파라미터 탐색, 최종 평가까지 머신러닝 워크플로를 구현한다.

**학습 자료:** 『핸즈온 머신러닝』

**핵심 학습 내용**
- 계층적 샘플링을 이용한 Train/Test 분할
- 결측치 처리 및 범주형 데이터 인코딩
- Pipeline과 ColumnTransformer 구성
- Linear Regression 및 Random Forest 학습
- Cross Validation과 GridSearchCV
- 데이터 누수 및 과적합 분석
- 전처리 방법에 따른 성능 비교

## 2. 데이터셋

California Housing 데이터셋을 사용했다.

| 항목 | 값 |
|---|---|
| 전체 샘플 | 20,640 |
| 전체 컬럼 | 10 |
| Train | 16,512 |
| Test | 4,128 |
| 입력 특성 | 9개 |
| 타깃 | `median_house_value` |

`median_income`을 기준으로 소득 범주(`income_cat`)를 생성하고, `StratifiedShuffleSplit`을 이용해 계층적 샘플링을 수행했다.

이를 통해 훈련셋과 테스트셋의 소득 범주 분포가 유사하도록 구성했다.

## 3. 데이터 전처리

### Numeric Features

8개의 숫자형 특성에 다음 전처리를 적용했다.

1. `SimpleImputer(strategy="median")` — 결측치 대체
2. `StandardScaler()` — 특성 표준화

### Categorical Features

`ocean_proximity`에 `OneHotEncoder(handle_unknown="ignore")`를 적용했다.

5개의 범주가 5개의 이진 특성으로 변환되었으며, 최종 전처리 데이터의 크기는 `(16512, 13)`이다.

숫자형·범주형 전처리는 `ColumnTransformer`로 통합하고, 모델과 함께 `Pipeline`으로 구성했다.

## 4. 모델 학습 및 평가

Linear Regression과 Random Forest를 비교했다.

평가 지표는 RMSE(Root Mean Squared Error)이며, 5-Fold Cross Validation을 사용했다.

| Model | 5-Fold CV RMSE |
|---|---:|
| Linear Regression | $69,218.40 |
| Random Forest (100 trees) | $49,941.18 |

Random Forest는 Linear Regression 대비 약 27.8% 낮은 RMSE를 기록했다.

또한 Random Forest에 대해 GridSearchCV를 수행했다.

- `n_estimators`: 50, 100
- `max_depth`: 10, 20, None
- CV: 5-Fold
- 최적 조합: `n_estimators=100`, `max_depth=None`

### 최종 모델 평가

| Dataset | RMSE |
|---|---:|
| Train | $18,342.37 |
| Cross Validation | $49,941.18 |
| Test | $47,197.67 |

최종 Test MAE는 **$30,929.48**이었다.

Train RMSE와 CV RMSE 사이에 큰 차이가 나타났으며, 이는 모델이 훈련 데이터에 과적합되었을 가능성을 보여준다.

테스트셋은 최종 모델 평가에 사용했으며, 모델 선택 과정에는 사용하지 않았다.

## 5. 추가 실험 — StandardScaler vs RobustScaler

전처리 방법에 따른 성능 변화를 확인하기 위해 Linear Regression의 숫자형 스케일러를 변경했다.

다른 조건은 동일하게 유지하고 5-Fold CV RMSE를 비교했다.

| Scaler | CV RMSE |
|---|---:|
| StandardScaler | $69,218.40 |
| RobustScaler | $69,218.40 |

두 방법의 결과는 수치 오차 수준을 제외하면 동일했다.

이는 절편을 포함한 비정규화 선형회귀에서 특성별 선형 스케일 변환이 회귀계수에 의해 보상될 수 있다는 이론과 일치한다.

따라서 이번 실험에서는 RobustScaler가 예측 성능을 개선하지 않았다.

## 6. 주요 학습 내용

### 데이터 누수 방지

전처리를 교차 검증 이전에 전체 데이터에 적용하면 검증 데이터의 정보가 학습 과정에 반영될 수 있다.

이를 방지하기 위해 전처리와 모델을 하나의 Pipeline으로 구성하고, Pipeline 전체를 교차 검증에 전달했다.

### 교차 검증

단일 Train/Validation 분할에 의존하지 않고 여러 Fold에서 모델 성능을 평가했다.

### 과적합 분석

훈련 성능이 높다는 사실만으로 일반화 성능이 좋다고 판단할 수 없다.

Train RMSE와 CV RMSE의 차이를 확인하여 과적합 가능성을 분석했다.

### 통제된 실험

전처리 방법의 영향을 확인할 때 모델과 평가 조건을 동일하게 유지했다.

이를 통해 실험 결과의 차이를 특정 변경 사항과 연결해 해석하는 방법을 학습했다.

## 7. 독립 구현

교재 실습 이후 별도의 `rebuild.ipynb`에서 다음 과정을 다시 구현했다.

- 데이터 로딩 및 탐색
- 계층적 Train/Test 분할
- 입력 특성과 타깃 분리
- 결측치 처리 및 인코딩
- Pipeline과 ColumnTransformer 구성
- Linear Regression 학습 및 교차 검증
- Random Forest 학습 및 교차 검증

추가로 `experiment.ipynb`에서 전처리 방법 비교 실험을 진행하는 것을 목표로 했다.

## 8. 회고

이번 미션을 통해 머신러닝 모델의 성능뿐 아니라 데이터 분할, 전처리, 평가 절차의 중요성을 학습했다.

특히 Pipeline을 사용하면 전처리와 모델 학습을 하나의 재현 가능한 과정으로 관리할 수 있으며, 교차 검증 과정에서 발생할 수 있는 데이터 누수를 방지할 수 있다는 점을 이해했다.

또한 Random Forest가 Linear Regression보다 높은 예측 성능을 보이더라도, 훈련 성능과 검증 성능을 함께 확인해야 한다는 점을 배웠다.

**다음 미션:** 분류(Classification) 문제를 통해 분류 모델의 학습 및 평가 방법을 익힌다.