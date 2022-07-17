# 판다스(PANDAS)

- 파이썬에서 데이터 처리를 위해 존재하는 라이브러리
- 서로 다른 형식을 갖는 여러 종류의 데이터를 컴퓨터가 이해할 수 있도록 동일한 형식을 갖는 구조로 통합할 필요가 있음
- 일반적으로 대부분 데이터 셋은 행(Row) X 열(Column)로 구성된 2차원 데이터로 구성
- 행과 열의 2차원 데이터가 인기 있는 이유는 인간이 가장 이해하기 쉬운 데이터 구조이면서 효과적으로 데이터를 담을 수 있는 구조이기 때문
- 2차원 데이터를 효율적으로 가공/처리할 수 있는 다양한 기능을 제공
- 판다스는 시리즈(Series)와 데이터프레임(DataFrame)이라는 데이터 형식을 제공
- 판다스 주요 구성 요소 - `DataFrame`, `Series`, `Index`

![image-20220330170615901](PANDAS.assets/image-20220330170615901.png)

---

### 1. 시리즈(Series)

- 데이터가 순차적으로 나열된 `1차원 배열(열벡터)`
- `인덱스(index)`는 `데이터 값(value)`과 일대일 대응
- 시리즈의 인덱스는 데이터 값의 위치를 나타내는 이름표(주소) 역할
- `딕셔너리`와 시리즈의 구조가 비슷하기 때문에 딕셔너리를 시리즈로 변환하는 방법을 많이 사용
- `PANDAS`의 내장 함수인 `Series()` 사용
  - 딕셔너리를 함수의 인자로 전달
- 딕셔너리를 시리즈로 변환하는 예제

```python
# 판다스 import
import pandas as pd

# key:value 를 쌍으로 갖는 딕셔너리를 생성, 변수 dict_data에 저장
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}

# 판다스 Series() 함수로 딕셔너리를 시리즈로 변환, 변수 sr에 저장
sr = pd.Series(dict_data)

# sr의 자료형 출력
print(type(sr))  # <class 'pandas.core.series.Series'>

# 변수 sr에 저장되어 있는 시리즈 객체 출력
print(sr)
'''
a	1
b	2
c	3
dtype: int64
'''
```

> - 시리즈 객체 출력 시 인덱스 'a', 'b', 'c'는 왼쪽에 표시
> - 인덱스와 짝을 이루는 데이터 값 1, 2, 3은 오른쪽에 표시
> - 시리즈를 구성하는 데이터 값의 자료형은 정수형(int64)
> - `"as pd"`는 판다스를 `"pd"`라는 약칭으로 부르겠다는 뜻
> - 인덱스는 자기와 짝을 이루는 데이터 값의 순서와 주소를 저장
> - 인덱스를 활용하여 데이터 값의 탐색, 정렬, 선택, 결합 등 데이터의 조작을 쉽게 할 수 있음

- 리스트를 시리즈로 변환하는 예제

```python
import pandas as pd

# 리스트 생성, 변수 list_data에 저장
list_data = ['2022-02-21', 3.14, '홍길동', 100, True]
sr = pd.Series(list_data)

print(sr)

# 결과값
'''
0    2022-02-21
1          3.14
2           홍길동
3           100
4          True
dtype: object
'''
```

> - 인덱스를 별도로 정의하지 않았기 때문에 디폴트로 정수형 위치 인덱스(0, 1, 2, 3, 4)가 자동 적용
> - 시리즈를 구성하는 원소 데이터 값의 자료형은 문자열(object)
>   - 숫자와 문자열이 데이터에 혼합되어 있을 경우 자료형이 문자열로 표기
> - 리스트와 판다스의 시리즈는 둘 다 동일하게 인덱스를 소유
>   - 리스트는 정수형 위치 인덱스만 존재
>   - ex) list_data[0]
> - 시리즈는 정수형 위치 인덱스와 인덱스 이름 둘 다 존재
>   - ex1) sr[o]
>   - ex2) sr['날짜']
> - 시리즈의 index/values 속성을 이용하여 데이터 값 따로 선택 가능

- 시리즈의 인덱스와 데이터를 따로 확인하는 예제

```python
import pandas as pd

list_data = ["2022-02-21", 3.14, "홍길동", 100, True]
sr = pd.Series(list_data)

# 인덱스 배열은 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print(val)

print(type(val))

'''
출력값

RangeIndex(start=0, stop=5, step=1)
['2022-02-21' 3.14 '홍길동' 100 True]
<class 'numpy.ndarray'>
'''
```

> - 인덱스는 0 ~ 4 범위의 정수를 갖는 RangeIndex 객체로 출력
> - 데이터 값은 1차원 배열 형태(array)로 출력



### 2. 데이터 프레임(DataFrame)

- 2차원 배열

- 여러 개의 열벡터(시리즈)들이 같은 행 인덱스를 기준으로 결합된 2차원 벡터 또는 행렬(matrix)

- 행과 열을 나타내기 위해서는 행 인덱스와 열 이름 두가지 종류의 주소를 사용

  - 열은 공통의 속성을 갖는 일련의 데이터의 집합
  - 행은 공통적이고 다양한 속성 데이터들의 모음인 레코드(record)

- 데이터프레임 만들기 전 생각해보기

  1.  데이터프레임을 만들기 위해서는 같은 길이의 1차원 배열(Series)이 여러개 필요

  2.  딕셔너리 값에 해당하는 각 리스트가 시리즈 배열로 변환되어 데이터 프레임의 열이 됨

  3.  딕셔너리 키는 각 시리즈의 이름으로 변환되어 데이터프레임의 열 이름이 됨

  4. 데이터프레임을 만들 때는 판다스 DataFrame() 함수를 사용

     <u><b>`딕셔너리 -> 데이터프레임 변환: pandas.DataFrame(딕셔너리 객체)`</b></u>

- 딕셔너리 -> 데이터프레임 변환 예제

```python
import pandas as pd

# key:value를 쌍으로 갖는 딕셔너리를 생성, 변수 dict_data에 저장
dict_data = {'c0': [1, 2, 3], 'c1' : [4, 5, 6], 'c2' : [7, 8, 9], 'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환, 변수 df에 저장
df = pd.DataFrame(dict_data)

print(type(df))	# <class 'pandas.core.frame.DataFrame'>

print(df)
'''
   c0  c1  c2  c3  c4
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15
'''
```

- 행 인덱스/열 이름 설정

  - 2차원 배열 -> 데이터프레임 변환할 때 행 인덱스와 열 이름 속성을 사용자가 직접 지정 가능

    <u><b>`행 인덱스, 열 이름 설정: pandas.DataFrame(2차원 배열, index=행 인덱스 배열, columns=열 인덱스 배열)`</b></u>

- 행 인덱스 / 열 이름 설정 예제

```python
import pandas as pd

# 행 인덱스 / 열 이름을 지정하여 데이터프레임 만들기
df = pd.DataFrame([[22, '남', '인천대'], [21, '여', '경기대'], [20, '남', '부산대']],
                  index=['규석', '영신', '성민'],
                  columns=['나이', '성별', '학교'])

print(df)
'''
    나이 성별   학교
규석  22  남  인천대
영신  21  여  경기대
성민  20  남  부산대
'''


print(df.index)		# Index(['규석', '영신', '성민'], dtype='object')
print(df.columns)	# Index(['나이', '성별', '학교'], dtype='object')
```

- 행 인덱스 / 열 이름 변경

  <u><b>`행 인덱스 변경: DataFrame 객체.index = 새로운 행 인덱스 배열`</b></u>

  <u><b>`열 이름 변경: DataFrame 객체.columns = 새로운 열 이름 배열`</b></u>

- 행 인덱스 / 열 이름 변경 예제

```python
import pandas as pd

# 행 인덱스 / 열 이름을 지정하여 데이터프레임 만들기
df = pd.DataFrame([[22, '남', '인천대'], [21, '여', '경기대'], [20, '남', '부산대']],
                  index=['규석', '영신', '성민'],
                  columns=['나이', '성별', '학교'])

df.index = ['준서', '지연', '성철']
df.columns = ['연령', '남녀', '소속']

print(df)

'''
    연령 남녀   소속
준서  22  남  인천대
지연  21  여  경기대
성철  20  남  부산대
'''

print(df.index)		# Index(['준서', '지연', '성철'], dtype='object')
print(df.columns)	# Index(['연령', '남녀', '소속'], dtype='object')
```



- `rename()` 함수를 사용하여 행 인덱스 / 열 이름 변경 가능

  <u><b>`행 인덱스 변경: DataFrame 객체.rename(index={기존 인덱스:새 인덱스, ...})`</b></u>

  <u><b>`열 이름 변경: DataFrame 객체.rename(columns={기존 열 이름:새 열 이름, ...})`</b></u>

  

- 행 인덱스 / 열 이름 변경 예제(rename)

```python
import pandas as pd

# 행 인덱스 / 열 이름을 지정하여 데이터프레임 만들기
df = pd.DataFrame([[22, '남', '인천대'], [21, '여', '경기대'], [20, '남', '부산대']],
                  index=['규석', '영신', '성민'],
                  columns=['나이', '성별', '학교'])

df.rename(index={'규석':'준서', '영신':'지연', '성민':'성철'}, inplace = True)
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace = True)

print(df)
'''
    연령 남녀   소속
준서  22  남  인천대
지연  21  여  경기대
성철  20  남  부산대
'''
```

> - inplace = True 를 쓰지 않으면 기존 객체가 변경되지 않음(기존 객체에 반영하기 위해 필수적으로 써줘야 됨)



- 행 / 열 삭제
  - 행 / 열 삭제 시 drop() 함수 사용
  - 행을 삭제할 때 축(axis) 옵션으로 axis=0 혹은 입력 X
  - 열을 삭제할 때 축(axis) 옵션으로 axis=1

행 / 열 삭제 예제

- 행 삭제 예제

```python
import pandas as pd

exam_data = {'국어' : [70, 90, 80], '수학' : [90, 85, 80], '영어' : [100, 80, 90], '음악' : [70, 90, 100]}
df = pd.DataFrame(exam_data, index=['인서', '형준', '소진'])

# 데이터프레임 df를 복제하여 변수 df2에 저장.
df2 = df

# 데이터프레임 df를 복제하여 변수 df3에 저장.
df3 = df

# df2의 1개 행(row) 제거
df2.drop(['인서'], axis = 0)
```

![image-20220718003606074](PANDAS.assets/image-20220718003606074.png)

```python
# df2의 2개 행(row) 제거
df3.drop(['형준', '소진'], axis = 0)
```

![image-20220718003722045](PANDAS.assets/image-20220718003722045.png)



- 열 삭제 예제

```python
import pandas as pd

exam_data = {'국어' : [70, 90, 80], '수학' : [90, 85, 80], '영어' : [100, 80, 90], '음악' : [70, 90, 100]}
df = pd.DataFrame(exam_data, index=['민혜', '재헌', '숙현'])

# 데이터프레임 df를 복제하여 변수 df2에 저장.
df2 = df

# 데이터프레임 df를 복제하여 변수 df3에 저장.
df3 = df

# df2의 1개 열(column) 삭제
df2.drop('국어', axis = 1)
```

![image-20220718003810711](PANDAS.assets/image-20220718003810711.png)

```python
# df3의 2개 열(column) 삭제
df3.drop(['영어', '음악'], axis = 1)
```

![image-20220718003830359](PANDAS.assets/image-20220718003830359.png)