# 앙상블 학습 (Ensemble Learning)

## Ensemble

![image-20221013154014584](Ensemble_Learning.assets\image-20221013154014584.png)

- 서로 다른 객체 학습기들로 구성

- 일련의 예측기(즉, 분류나 회귀 모델)로 부터 예측을 수직하면 가장 좋은 모델 하나보다 더 좋은 예측을 얻을 수 있다.

  ![image-20221013154118453](Ensemble_Learning.assets\image-20221013154118453.png)

  ![image-20221013154129567](Ensemble_Learning.assets\image-20221013154129567.png)



#### 동질적 객체 학습기

- 같은 객체 학습기를 사용하는 방법
- Random Forest



#### 이질적 객체 학습기

- 서로 다른 객체 학습기를 사용하는 방법

- Forest + Neural Network

  ![image-20221013154249512](Ensemble_Learning.assets\image-20221013154249512.png)



#### 객체 학습기 사이의 관계

- 각 학습기들간의 의존관계에 따라서 Model이 분류된다.
- 강한 의존관계
  - Serial로 생성되는 연속적인 방법으로 분류가 진행됨
  - Boosting
- 약한 의존관계
  - 동시에 생성가능한 Parallel 한 방법으로 학습이 진행됨
  - Bagging, RandomForest



#### 객체 학습기의 훈련 상태와 성능의 관계

- 각 객체 학습기의 성능이 Ensemble 모델 성능에 영향을 미친다.

  ![image-20221013154502655](Ensemble_Learning.assets\image-20221013154502655.png)

  ![image-20221013154518351](Ensemble_Learning.assets\image-20221013154518351.png)





## Sampling

#### Bootstrapping

![image-20221013154553790](Ensemble_Learning.assets\image-20221013154553790.png)

![image-20221013154605914](Ensemble_Learning.assets\image-20221013154605914.png)

- 각 객체 학습기는 서로 다른 Train Data Set을 사용

- 복원추출(Sampling with replacement)을 통해 원래 데이터의 크기만큼을 갖도록 Sampling한다.

- 이때 복원추출된 각각의 개별 DataSet을 Bootstrap Set이라고 부른다.

- 복원 추출이지만 한 개의 Dataset이 Bootstrap이 선택되지 않을 확률은 0.368이다.

  ![image-20221013154743310](Ensemble_Learning.assets\image-20221013154743310.png)



## Aggregation

- 결과를 취합하는 방식



#### Majority Voting(Hard Voting)

- 가장 많이 투표된 값으로 선택

  ![image-20221013154852712](Ensemble_Learning.assets\image-20221013154852712.png)



#### Probability Voting(Soft Voting)

- 각 Class가 내놓은 예측 확률값의 평균

  ![image-20221013154950553](Ensemble_Learning.assets\image-20221013154950553.png)



#### Weighted Voting

- 각 Class별 지정된 weight로 사용해 판단한다.

- Weight는 training accuracy 등을 사용할 수 있다.

  ![image-20221013155043025](Ensemble_Learning.assets\image-20221013155043025.png)



## Voting Classifier

- Basic Ensemble Classifier

- 정확도가 80%인 분류기 여러 개를 훈련시켰다고 가정 : 로지스틱 회귀 분류기, SVM 분류기, 랜덤 포레스트 분류기, K-최근접 이웃 분류기 등

  ![image-20221013155240133](Ensemble_Learning.assets\image-20221013155240133.png)



#### Hard voting

- 직접 투표(hard voting) 분류기 : 다수결 투표로 정해지는 분류기. 더 좋은 분류기를 만드는 매우 간단한 방법은 각 분류기의 예측을 모아서 가장 많이 선택된 클래스를 예측하는 것
- 강한 학습기
- 약한 학습기
- 큰 수의 법칙



## Ensemble의 종류

- Bagging
  - (Bagging)Random Forest
- Pasting
- Boosting
  - AdaBoost(Adaptive Boost)
  - Gradient Boosting
  - XGBoost
  - LightGBM
  - GLMBoost
- Staking



## 배깅(bagging, bootstrap aggregating)과 페이스팅(pasting)

- 같은 알고리즘을 사용하고 훈련 세트의 서브셋을 무작위로 구성하여 분류기를 각기 다르게 학습

- 사이킷런의 배깅과 페이스팅

  - 사이킷런 API: BaggingClassifier(회귀의 경우에는 BaggingRegressor)

    ![image-20221013155657860](Ensemble_Learning.assets\image-20221013155657860.png)



## 랜덤 패치와 랜덤 서브스페이스

#### BaggingClassifier는 특성 샘플링도 지원

- 작동 방식은 max_samples, bootstrap과 동일하지만 샘플이 아니고 특성에 대한 샘플링
  - 샘플링은 max_features, bootstrap_features 두 매개변수로 조절
  - 각 예측기는 무작위로 선택한 입력 특성의 일부분으로 훈련
- 매우 고차원의 데이터셋을 다룰 때 유용
- 랜덤 패치 방식
  - 훈련 특성과 샘플을 모두 샘플링
- 랜덤 서브스페이스 방식
  - 훈련 샘플을 모두 사용하고(bootstrap=False이고 max_samples=1.0로 설정) 특성은 샘플링(bootstrap_features=True 그리고/또는 max_features는 1.0보다 작게 설정)
- 특성 샘플리은 더 다양한 예측기를 만들며 편향을 늘리는 대신 분산을 낮춤



#### 코드

- (최대 16개의 리프 노드를 갖는) 500개 트리로 이뤄진 랜덤 포레스트 분류기를 여러 CPU 코어에서 훈련시키는 코드

  ![image-20221013160105126](Ensemble_Learning.assets\image-20221013160105126.png)