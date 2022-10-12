# SVM (Support Vector Machine)

### 도입

- 아래와 같은 데이터 셋이 주어졌을때 어떻게 분류 해야 할까?

  - 하나의 선형모델을 찾고 서로다른 Class의 Sample을 분리한다.

  - 하지만 여러개의 선형모델이 존재한다면 어떤게 더 좋은 방법일까?

  - L(1), L(2), L(3) 중 어느 직선을 사용해야 할까?

    ![image-20221012200814296](SVM.assets/image-20221012200814296.png)

- Question

  - Model  -->   Training(&Generalization)시 데이터 예측에 대한 성능이 좋아져야 한다.
  - 하지만 Training Data에 대한 성능이 높아지면 Generalization 성능은 낮아지게 된다. 이를 해결 할 수 없을까?



### 분류문제

- 기본적인 분류문제 : 3차원, 분류, 선형

  ![image-20221012200949710](SVM.assets/image-20221012200949710.png)

- 2차원에서 두 개의 클래스를 가장 잘 분류한 직선은 무엇일까?

  - 두 개의 Class를 나누는 평면은 무수히 많지만 어떻게 나눠야 최적화된 평며이 만들어 질까?

  - <b>좋음</b>의 기준은 무엇인가?

    ![image-20221012201056235](SVM.assets/image-20221012201056235.png)

### Sample Space

![image-20221012201132032](SVM.assets/image-20221012201132032.png)



### 선형 SVM 분류

- 라지마진 분류 (maximizing margin over the training set)

  - SVM에서 <b>좋음</b>의 기준은 Margin 이다.
  - <b>Margin을 최대화</b> 시키는 Hyperplane을 찾는다.
  - Minimizing generalization error(=testing error)  ==> 좋은 예측 성능을 나타낸다.

- Margin 이란?

  - 각 class에서 가장 가까운 관측치 사이의 거리를 나타낸다.

  - Margin은 W(기울기)로 표현 가능

    ![image-20221012201427311](SVM.assets/image-20221012201427311.png)

  - 경계에 위치한 샘플을 <b>서포트 벡터</b>라고 한다.

    ![image-20221012201456802](SVM.assets/image-20221012201456802.png)



### 하드 마진  vs  소프트 마진

![image-20221012201533331](SVM.assets/image-20221012201533331.png)

- 하드 마진 분류 : 모든 샘플이 쪽(오른 or 왼 or 위 or 아래)으로 올바르게 분류되어 있는 경우

  - 왼쪽 그래프 : 하드 마진을 찾을 수 없는 경우
  - 오른쪽 그래프 : 결정 경계에 이상치가 없어 결정경계가 매우 일반화 되어 있는 경우

  ![image-20221012201740808](SVM.assets/image-20221012201740808.png)



### 비선형 SVM 분류

- 비선형 데이터 셋을 다루는 방법

  - 더 높은 차원의 특성 공간으로 투영하여 특성공간 내에서 선형 분리 가능하게 만들 수 있다.

    ![image-20221012201840461](SVM.assets/image-20221012201840461.png)