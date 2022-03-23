# NUMPY

- `Numerial Python`
- 산술 계산을 위한 패키지
  - 다차원 배열인 `ndarray` 는 빠른 배열 계산을 제공
  - 반복문을 작성할 필요 없이 전체 데이터 배열을 빠르게 계산할 수 있는 표준 수학 함수
  - 선형대수, 난수 생성시, 푸리에 변환 등 가능
- 일반적인 산술 데이터 처리를 위한 기본 라이브러리 제공
  - 연산 처리 후 통계나 분석데이터를 처리하기 위해선 `Pandas`를 사용
- 파이썬 산술 계산 영역에서 중요한 위치를 차지하는 이유 중 하나는 대용량 데이터 배열을 효율적으로 다룰 수 있도록 설계되어 있기 때문
- `Numpy` 사용 예제

```python
import numpy as np	# 보통 np로 많이 씀

my_arr = np.arange(1000000)
my_list = list(range(1000000))
```

- 1차원 배열 생성

```python
print(type(my_arr))		# <class 'numpy.ndarray'>
print(type(my_list))	# # <class 'list'>
```

```python
# 타입 뿐만 아니라 출력 했을때 모양이 비슷한듯 다름
print(my_arr)	# [ 0 1 2 3 ... 999999 ]
print(my_list)	# [0, 1, 2, 3, ..., 999999]

# array는 띄어쓰기로만 구분 list는 쉼표(,)로 구분
```

- 다차원 배열 객체

  - `Numpy`는 `ndarray` 라고 하는 N차원 배열 객체를 사용

    - 1차원 : `Vector`
    - 2차원 : `Matrix`
    - 3차원 : `Tensors`

    ![image-20220323165048893](C:\Users\GHW\AppData\Roaming\Typora\typora-user-images\image-20220323165048893.png)

- `ndarray`

  - `ndarray` 형태(shape)와 차원

  - | array                  | 차원   | shape  |
    | ---------------------- | ------ | ------ |
    | [1 2 3]                | 1 차원 | (3, )  |
    | ([1 2 3]<br />[4 5 6]) | 2 차원 | (2, 3) |

    - `ndarray`의 shape은 `ndarray.shape` 속성으로, 차원은 `ndarray.ndim` 속성으로 알 수 있음

  - `ndarray` 생성하기 예제(list -> array)

  ```python
  import numpy as np
  
  data1 = [5, 7, 8, 1, 4]
  type(data1)		# list
  arr1 = np.array(data1)
  type(arr1)		# numpy.ndarray
  print(arr1)		# [5 7 8 1 4]
  ```

  - 2차원 배열 생성 예제

  ```python
  import numpy as np
  
  arr1 = np.array([[1, 2, 3], [4, 5, 6]])		# 2차원을 할때 대괄호('[]')를 한 번 더 써줘야 댐
  print(arr1)
  '''
  <출력값>
  [[1 2 3]
  [4 5 6]]
  '''
  ```

  