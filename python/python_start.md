### 1. 기초 문법

##### 1.1 출력문

- print() 함수 예제

```python
# "hello world라는 문자열을 출력"
print("hello world")

a = 10	# a에 10이라는 값을 넣어줌
b = 20	# b에 20이라는 값을 넣어줌

print(a + b)	# a와 b의 합인 30을 출력
```

- 파이썬에서는 파일화 시킬 때 반드시 print() 함수를 써줘야 한다
  - ex) print(a + b) O
  - ex) a + b  X

```python
print("life" "is" "short")	# "lifeisshort"로 출력되어 나옴

pirnt("life", "is", "short")	# ','(콤마)로 구분해주면 띄어쓰기가 되어서 나옴
								# "life is short" 출력
print("life is short")	# 띄어쓰기를 처음부터 넣어주는 방법
```

- input()
  - input은 값을 따로 입력 받아 그 값을 출력해줌

```python
a = input("a 값을 입력해주세요 : ")	# 입력한 값을 a에 저장

# 20을 입력한 후 a 출력
print(a)
```



##### 1.2 주석

- 주석은 코드의 설명을 하거나 출력하고 싶지 않은 문장을 넣을 때 사용

- 주석 사용 예제 1

```python
identity = "지구인"	# 정체 1
number_of_legs = 10	# 다리의 수
print(identity)
print(number_of_legs)

# '정체 1'과 '다리의 수'는 출력되지 않음
```

- 주석 사용 예제 2

```python
# 주석

"""
주석 내용입니다.
"""
print("hello")
```

- 두 줄이상 주석은 큰 따옴표(") 3개 혹은 작은 따옴표(') 3개 사용

##### 1.3 변수

- 변수란? 연산을 위해 자료를 보관하는 곳
- 변수의 특징
  - 변수명의 첫 문자는 _(언더바), 영문자 등으로 시작할 수 있으며 특수문자(@#$!%...), 예약어는 사용할 수 없다.
  - 똑같은 이름의 변수에 새로운 값을 저장할 셩우 변수의 값이 변경 X, 새로운 변수가 생성 O
    - 기존 변수의 값 위에 새로운 값이 덮어 씌어지기 때문에 불러 올 수 없음 
- 변수 생성 특징 예제

```python
identity = "지구인"
identity = "외계인"
print(identity)		# "외계인"이 출력


1_unit = 1		# 변수명이 숫자로 시작하여 에러발생

_unit = 1		# 변수명이 언더바(_)로 시작하기 때문에 문제없음

@unit = 1		# 변수명이 특수문자로 시작하여 에러 발생

and = 1			# 변수명이 예약어라 사용불가
for = 1			# 변수명이 예약어라 사용불가
```

- 변수 제거 예제(del함수)

```python
a = 3	# a에 3을 넣어줌
b = 4	# b에 4를 넣어줌

print(a)	# 3출력
print(b)	# 4출력

del(a)		# 변수 a 제거
del(b)		# 변수 b 제거

print(a)	# a를 제거했기 때문에 print()함수로 출력 되지 않음
print(b)	# b를 제거했기 때문에 print()함수로 출력 되지 않음
```

##### 1.4 비교 연산자 예제

- 비교연산자( >, <, >=, <=)는 True나 False값이 출력값으로 나옴

```python
X = 3
Y = 4
print(X < Y)	# True 출력
print(X > Y)	# False 출력
```

- in, not in 예제
  - in : 자료에 있는지 여부를 확인(True, False로 출력)
  - not in : 자료에 없는지 여부를 확인(True, False로 출력)

```python
print(1 in [1, 2, 3])	# 1이 리스트안에 속하므로 True 출력
print(1 not in [1, 2, 3])	# 1이 리스트안에 속하므로 False 출력

print('a' in ('a', 'b', 'c'))	# True 출력

print('j' in 'python')	# 리스트나 튜플이 아닌 문자열에서도 찾기 가능
```

