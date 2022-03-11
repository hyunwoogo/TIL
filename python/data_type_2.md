### 자료형

##### 1. 리스트

- 여러 요소값을 담을 수 있는 자료형

- `\[](대괄호)`를 이용하여 생성

- 리스트는 빈 리스트 일수도 있고 어떠한 자료형도 포함시킬 수 있다

  - 생성예제

  ```python
  a = [1, 2, 3]
  print(a)
  
  # [1, 2, 3] 출력
  ```

  - 리스트 인덱싱 예제

  ```python
  a = [1, 2, 3]
  print(a[0]) # 0번 자리 1출력
  
  print(a[0] + a[2])	# 1 + 3 값인 4출력
  
  print(a[-1])	# 뒤에서 첫번째 값 3출력
  ```

  ```python
  b = ['Life', 'is', 'too', 'short']
  print(b[0] + b[1])	# "Lifeis" 출력
  ```

  ```python
  a = [1, 2, 3, ['a', 'b', 'c']]	# 리스트 안에 리스트 하나 더 들어간 형태
  print(a[-1])	# ['a', 'b', 'c'] 출력
  print(a[3])		# 위 코드와 같음
  
  print(a[-1][0])	# ['a', 'b', 'c'] 중 0번자리 "a" 출력
  print(a[-1][1])	# ['a', 'b', 'c'] 중 1번자리 "b" 출력
  print(a[-1][2]) # ['a', 'b', 'c'] 중 3번자리 "c" 출력
  
  ```

  ```python
  a = [1, 2, ['a', 'b', ['life', 'is']]]	# 리스트안에 리스트안에 리스트
  
  print(a[2])	# "['a', 'b', ['life', 'is']]" 출력
  print(a[2][2])	# "['life', 'is']" 출력
  print(a[2][2][0])	# 'life' 출력
  
  ```

  - 리스트 슬라이싱 예제
  
  ```python
  a = [1, 2, 3, 4, 5]
  a[0:2]	# 0번부터 2번전까지 출력
  		# [1, 2] 출력
      
  b = a[:2]		# 위의 출력문과 같은 리스트값을 b에 넣음
  print(b)		# 처음부터나 끝까지는 생략가능
      
  c = a[2:]		# 2번자리부터 끝까지
  print(c)		# [3, 4, 5] 출력
  
  a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
  print(a[2:5])	# [3, ['a', 'b', 'c'], 4, 5]
  
  print(a[3])		# ['a','b', 'c']
  
  print(a[3][:2])	# ['a', 'b']
  
  ```
  
  - 리스트 합치기 예제
  
  ```python
  a = [1, 2, 3]
  b = [4, 5, 6]
  
  print(a + b)	# [1, 2, 3, 4, 5, 6] 출력
  
  ```
  
  - 리스트 반복 예제
  
  ```python
  a = [1, 2, 3]
  print(a*2)	# [1, 2, 3, 1, 2, 3] 출력
  ```
  
  - 리스트 요소 수정 예제
  
  ```python
  a = [1, 2, 3]
  print(a[2])		# 3 출력
  
  a[2] = 4	# 2번자리에 4를 넣음
  print(a)	# [1, 2, 4] 출력
  
  a[1:2]	= ['a', 'b', 'c']	# 1번자리 부터 2번자리 전에 'a', 'b', 'c' 넣음
  print(a)	# [1, 'a', 'b', 'c', 4] 출력
  
  a[0] = ['a1', 'a2', 'a3']	# 0번 자리에 ['a1', 'a2', 'a3'] 넣음
  print(a)	# [['a1', 'a2', 'a3'], 'a', 'b', 'c', 4] 출력
  
  # 수정 할 때 인덱싱을 쓰면 리스트 형태로 들어가고 슬라이싱을 쓰면 값이 하나하나 들어감
  
  ```
  
  - 리스트 요소 제거 예제( `del` )
  
  ```python
  a = [['a1', 'a2', 'a3'], 'a', 'b', 'c', 4]
  a[1:3] = []		# 1번부터 3번자리 전까지 빈값을 넣음
  print(a)		#[['a1', 'a2', 'a3'], 'c', 4] 출력
  
  del a[1]	# del함수를 써서 1번자리 삭제
  print(a)	# [['a1', 'a2', 'a3'], 4] 출력
  
  del a[0:2]
  print[a]	# 안에 요소들을 다 지워서 빈리스트([]) 출력
  ```
  
  - 리스트 요소 추가 예제( `append` )
    - 리스트 가장 마지막 자리에 들어감
  
  ```python
  a = [1, 2, 3]
  a.append(4)
  print(a)	# append() 함수로 4를 넣어주었기 때문에 [1, 2, 3, 4] 출력
  
  a.append([5, 6])
  print(a)	# [1, 2, 3, 4, [5, 6]] 출력
  ```
  
  - 리스트 정렬 예제( `sort` )
    - 디폴트 값으로 오름차순이 설정되어 있음
    - 숫자 뿐만 아니라 영문자도 가능
    - 영문자일 경우 대문자가 먼저 정렬됨
  
  ```python
  a = [1, 4, 3, 2]
  a.sort()
  print(a)	# [1, 2, 3, 4] 출력
  
  a = ['abc', '123', 'you need python']
  a.sort()
  print(a)	# ['123', 'abc', 'you need python'] 출력
  
  a = ['abc', '123', 'You need python']
  a.sort()
  print(a)	# ['123', 'You need python', 'abc'] 출력
  
  ```
  
  ```python
  a = ['abc', 123, 'you need python']
  a.sort()
  
  # 에러 남(리스트 안에 자료들의 속성이 달라서 대소 비교할 수 없음)
  ```
  
  - 리스트 뒤집기 예제( `reverse` )
    - 대소 구분을 하지않고 원래 순서의 반대로만 정렬
  
  ```python
  a = ['a', 'c', 'b']
  a.reverse()
  print(a)	# ['b', 'c', 'a'] 출력
  ```
  
  - 리스트 요소 찾기 예제
  
  ```python
  a = [1, 2, 3]
  a.index(3)	# 3의 인덱스 값 2가 출력
  
  a.index(0)	# 리스트 안에 0이 존재하지 않아 에러 뜸
  ```
  
  - 리스트 요소 삽입 예제( `insert` )
    - `append`와 다르게 넣을 자리를 선택 할 수 있음
    - `insert("자리", "넣을 값")`
  
  ```python
  a = [1, 2, 3]
  a.insert(0, 4)	# 0번자리에 4 넣음
  print(a)	# [4, 1, 2, 3] 출력
  
  a.insert(3, 5)
  print(a)	# [4, 1, 2, 5, 3] 출력
  
  a.insert(0, ['a', 'b'])
  print(a)	# [['a', 'b'], 4, 1, 2, 5, 3] 출력
  ```
  
  - 리스트 요소 제거 예제( `remove` )
    - `remove(x)` : 리스트 내에 처음으로 나오는 x를 지움
  
  ```python
  a = [1, 2, 3, 1, 2, 3]
  a.remove(3)
  print(a)	# [1, 2, 1, 2, 3] 출력
  
  a.remove(3)
  print(a)	# [1, 2, 1, 2] 출력
  ```
  
  - 리스트 요소 끄집어내기 예제( `pop` )
    - 리스트 제일 끝 요소를 끄집어 내어 보여주고 그 요소를 삭제해 버리는 것이 기본
    - `pop(인덱스값)` 으로 원하는 자리를 끄집어 낼 수 있음
  
  ```python
  a = [1, 2, 3]
  a.pop()		# 3이 나오면서 출력이 됨
  print(a)	# 3이 삭제 되었기 때문에 [1, 2] 출력
  
  a = [1, 2, 3]
  a.pop(1)	# 1번 자리 끄집어 냄 2가 출력 됨
  print(a)	# [1, 3] 출력
  ```
  
  - 리스트 갯수 세기 예제( `count` )
  
  ```python
  a = [1, 2, 3, 1]
  a.count(1)	# 1이 2개 있기 때문에 2출력
  ```
  
  - 리스트 확장 예제( `extend` )
    - `extend(x)` 에서 x에는 리스트만 올 수 있음
  
  ```python
  a = [1, 2, 3]
  a.extends([4, 5])
  print(a)	# [1, 2, 3, 4, 5] 출력
  
  # 밑에 코드도 똑같은 출력값
  a = [1, 2, 3]
  b = [4, 5]
  c = a + b
  print(c)
  ```

---

##### 2. 튜플

- 튜플은 `()(소괄호)`를 사용하여 생성

- 튜플은 리스트와 유사하나, 읽기 전용

- 튜플은 요소를 지우거나 변경이 불가

- 리스트 안에 튜플을 넣어서 사용하는 경우가 많음
  - 리스트 안에서도 바뀌지 않는 요소가 있어야 하기 때문
  
- 읽기 전용인 만큼 함수도 리스트에 비해 적지만, 속도가 빠름
  
- 튜플의 요소가 하나일때 (요소,) 처럼 마지막에 쉼표(,) 찍어줘야 됨
  
  -  생성 예제
  
  ```python
  t1 = ()
  print(t1)
  
  print(type(t1))	# <class 'tuple'> 출력
  
  t2 = (1)
  print(t2)	# 1 출력
  print(type(t2))	# <class 'int'> 출력 괄호 마지막에 쉼표를 찍어주지 않아서
  
  t2 = (1, )
  print(t2)	# (1, ) 출력
  print(type(t2))	# <class 'tuple'> 출력
  
  t3 = (1, 2, 3)
  print(t3)
  
  t4 = 1, 2, 3
  print(t4)	# 튜플형태인 (1, 2, 3)으로 출력
  
  t5 = ('a', 'b', ('ab', 'cd'))
  print(t5)
  
  t6 = (1, 2, [3, 4])
  print(t6)
  
  ```
  
  - 튜플 요소 제거 예제
  
  ```python
  t1 = (1, 2, 'a', 'b')
  del t1[0]	# 에러남(튜플은 요소를 제거 할 수 없음)
  ```
  
  - 튜플 인덱싱/ 슬라이싱 예제
  
  ```python
  t1 = (1, 2, 'a', 'b')
  print(t1[0])	# 1출력
  
  print(t1[3])	# 'b'출력
  
  print(t1[1:])	# (2, 'a', 'b') 출력
  ```
  
  - 튜플 더하기 예제
  
  ```python
  t1 = (1, 2, 'a', 'b')
  t2 = (3, 4)
  
  print(t1 + t2)	# (1, 2, 'a', 'b', 3, 4) 출력
  
  t3 = t1 + t2
  print(t3)	# (1, 2, 'a', 'b', 3, 4) 출력
  ```
  
  - 튜플 곱하기 예제
  
  ```python
  t1 = (1, 2, 'a', 'b')
  t2 = (3, 4)
  
  print(t2 * 3)	# (3, 4, 3, 4, 3, 4) 출력
  
  t4 = t2 *3
  print(t4)	# (3, 4, 3, 4, 3, 4) 출력
  ```
  
  - 튜플 길이 구하기 예제
  
  ```python
  t1 = (1, 2, 'a', 'b')
  print(len(t1))	# 4 출력
  ```



- 튜플의 패킹과 언패킹

  - 패킹 : 한 데이터에 여러 개의 데이터를 넣는 것
    - 실습을 통해 만들어 본 리스트, 튜플 자료형이 패킹에 속함
  - 언패킹 : 한 데이터에서 데이터를 각각 꺼내오는 것
    - 튜플과 리스트 둘 다 패킹, 언패킹 가능
  - 언패킹 예제

  ```python
  T = (1, 2, 3, 4, 5)
  a, b, c, d, e = T
  print(a, b, c, d, e)	# 1 2 3 4 5 출력
  
  a, *b = T		# "*"의 의미는 나머지라는 뜻, 제일 처음 값만 a로 넣고 나머지는 b로
  print(a, b)		# 1 [2, 3, 4, 5] 출력
  
  a, b, *c = T
  print(a, b, c)	# 1 2 [3, 4, 5] 출력
  
  print(type(c))	# <class 'list'> 출력
  ```

  - 리스트 -> 튜플 변경 예제( `tuple함수` )

  ```python
  L = [1, 2, 3, 4, 5]
  T = tuple(L)
  print(T)	# (1, 2, 3, 4, 5) 출력
  ```

  - 튜플 -> 리스트 변경 예제( `list함수` )

  ```python
  T = (1, 2, 3, 4, 5)
  L = list(T)
  print(L)	# [1, 2, 3, 4, 5] 출력
  ```

---

##### 3. 딕셔너리

- `중괄호({})` 로 만듬

- key : value 형태의 한쌍으로 요소 들을 갖는다

  - 생성 예제 - 1

  ```python
  dic = {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'}
  print(dic)	# {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'} 출력
  
  a = {'a' : [1, 2, 3]}
  print(a)	# {'a' : [1, 2, 3]} 출력
  
  ```

  - 생성 예제 - 2 (함수( `dict` ) 사용)

  ```python
  a = dict(one = 1, two = 2)
  print(a)	# {'one' : 1, 'two' : 2} 출력
  
  b = dict([('one', 1), ('two', 2)])
  print(b)	# {'one' : 1, 'two' : 2} 출력
  
  keys = ['one', 'two', 'three']
  values = (1, 2, 3)
  zip(keys, values)
  d = dict(zip(keys, values))
  print(d)	# {'one' : 1, 'two' : 2, 'three' : 3} 출력
  ```
  
  
  
  - key, value 추가 예제
  
  ```python
  a = {1:'a'}
  a[2] = 'b'	# 2라는 키를 가진 'b'를 추가
  
  print(a)	# {1 : 'a', 2 : 'b'} 출력
  
  a['name'] = 'pey'
  print(a)	# {1 : 'a', 2 : 'b', 'name' : 'pey'} 출력
  
  a[3] = [1, 2, 3]
  print(a)	# {1 : 'a', 2 : 'b', 'name' : 'pey', 3 : [1, 2, 3]} 출력
  
  ```
  
  - 함수를 만들어서 키와 값으로 활용하기 예제
  
  ```python
  def add(a, b):
      return a + b	# 매개변수 a,b의 합을 반환하는 함수(add) 정의
  def sub(a, b):
      return a - b	# 매개변수 a,b의 차을 반환하는 함수(sub) 정의
  
  action = {0 : add, 1: sub}
  ```
  
  ```python
  action[0](4, 5)		# 9 출력
  ```
  
  - 딕셔너리 키 제거 예제
  
  ```python
  a = {1 : 'a', 2 : 'b', 'name' : 'pey', 3 : [1, 2, 3]}
  
  del a[1]	# 1이라는 키값을 가진 원소 제거 (리스트는 인덱스 값이 었지만 딕셔너리는 키값을 가리킴)
  print(a)	# {2 : 'b', 'name' : 'pey', 3 : [1, 2, 3]} 출력
  ```
  
  - 딕셔너리에서 키를 이용해 값을 얻기 예제
  
  ```python
  a = {1:'a', 2:'b'}
  print(a[1])		# 'a' 출력
  print(a[2])		# 'b' 출력
  ```
  
  - 키 리스트 만들기 예제
  
  ```python
  a = {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'}
  print(a.keys())		# key 값만 출력 (dict_keys(['name', 'phone', 'birth']))
  
  print(type(a.keys()))	# <class 'dict_keys'> 출력
  
  list(a.keys())
  
  for i in a.keys():		# 반복문으로 a.key() 리스트 요소 출력 
      print(i)
  ```
  
  - 값 리스트 만들기 예제
  
  ```python
  a = {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'}
  print(a.values())	# value 값만 출력 (dict_values(['pey', '01199993323', '1118']))
  ```
  
  - 딕셔너리 모든 요소 지우기 예제
  
  ```python
  a = {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'}
  a.clear()
  print(a)	# 빈 딕셔너리 {} 출력
  ```
  
  - 키를 이용해 값 출력하기 예제( `get() `)
  
  ```python
  a = {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'}
  print(a.get('name'))	# 'pey' 출력
  print(a.get('phone'))	# '01199993323' 출력
  
  print(a.get('foo'))		# 'foo'가 존재 하지 않아 None 출력
  
  print(a.get('foo', 'bar'))	# 'foo'가 없으면 'bar'출력 하라는 뜻
  ```
  
  > `get()` 함수의 사용 유무의 차이
  >
  > - 존재 하지 않는 키 값으로 찾으려고 할때
  >   - `get()` 함수 사용 :  ***None*** 출력
  >   - `get()` 함수 사용 X  :  ***Error 메시지***  뜸
  
  - 해당 키의 존재 유무 예제
  
  ```python
  a = {'name' : 'pey', 'phone' : '01199993323', 'birth' : '1118'}
  
  print('name' in a)	# 'name' 키가 있어서 True 출력
  
  print('email' in a)	# 'email' 키가 없어서 False 출력
  ```



---

##### 4. 집합

- `set()` 함수를 사용해서 생성

- 여러 값을 순서 없이 그리고 중복 없이 모아 놓은 자료형

- 리스트나 문자열로도 집합을 만들 수 있음

- 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음

  - 집합 생성 예제

  ```python
  s1 = set([1, 2, 3])
  print(s1)	# {1, 2, 3, 4} 출력
  s2 = set("Hello")
  print(s2)	# {'l', 'o', 'e', 'H'} : 중복값 제외되고 순서없이 나옴
  ```

  - 교집합( `intersection` ) 예제

  ```python
  s1 = set([1, 2, 3, 4, 5, 6])
  s2 = set([4, 5, 6, 7, 8, 9])
  
  # 1. 'intersection' 함수 사용 X
  print(s1 & s2)	# {4, 5, 6} 출력
  
  # 2. 'intersection' 함수 사용
  print(s1.intersection(s2))
  ```

  - 합집합( `union` ) 예제

  ```python
  s1 = set([1, 2, 3, 4, 5, 6])
  s2 = set([4, 5, 6, 7, 8, 9])
  
  # 1. 'union' 함수 사용 X
  print(s1 | s2)	# {1, 2, 3, 4, 5, 6, 7, 8, 9} 출력
  
  # 2. 'union' 함수 사용
  print(s1.union(s2))
  ```

  - 차집합( `difference` ) 예제

  ```python
  s1 = set([1, 2, 3, 4, 5, 6])
  s2 = set([4, 5, 6, 7, 8, 9])
  
  # 1. 'difference' 함수 사용 X
  print(s1 - s2)	# {1, 2, 3} 출력
  
  # 2. 'difference' 함수 사용
  print(s1.difference(s2))
  
  print(s2 - s1)	# {7, 8, 9} 출력
  print(s2.difference(s1))
  
  ```

  - 집합에 값 1개 추가 하기 ( `add `)

  ```python
  s1 = set([1, 2, 3])
  s1.add(4)
  print(s1)	# {1, 2, 3, 4}
  ```

  - 집합에 값 여러개 추가 하기( `update `)

  ```python
  s1 = set([1, 2, 3])
  s1.update([4, 5, 6])
  print(s1)	# {1, 2, 3, 4, 5, 6}
  ```

  - 집합에 특정 값 제거 예제( `remove` )

  ```python
  s1 = set([1, 2, 3])
  s1.remove(2)
  print(s1)	# {1, 3}
  ```

  
