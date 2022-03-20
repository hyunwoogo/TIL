# 내장함수 / 외장함수

### 1. 내장함수

- 파이썬 내장 함수는 외부 모듈과 달리 `import`가 필요하지 않기 때문에 아무런 설정 없이 바로 사용 가능

  1. `abs()`

     - `abs(x)` 는 어떤 숫자를 입력 받았을 때, 그 숫자의 절댓값을 돌려주는 함수

     ```python
     abs(3)		# 3출력
     abs(-3)		# 3출력
     abs(-1.2)	# 1.2출력
     ```

  2.  `all()`

     - `all(x)`는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며  이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False 리턴
     - 반복 가능한 자료형이란 `for문` 으로 그 값을 출력할 수 있는 것을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등

     ```python
     all([1, 2, 3])	# True 출력
     all([1, 2, 3, 0])	# False 출력
     ```

  3.  `any()`

     - `any(x)`는 x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일때만 False를 리턴

     ```python
     any([1, 2, 3, 0])	# True 출력
     any([0, ""])	# False 출력
     ```

  4. `chr()`

     - `chr(i)`는 **아스키(ASCII)** 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수

     ```python
     chr(97)	# 'a'출력
     chr(48)	# '0' 출력, 문자열로 '0'임 정수형 0과는 다름
     ```

  5. `dir()`

     - `dir`은 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌

     ```python
     dir([1, 2, 3])	# 리스트 객체 관련 함수를 출력
     
     dir({'1':'a'})	# 딕셔너리 객체 관련 함수를 출력
     ```

  6. `divmod()`

     - `divmod(a, b)`는 2개의 숫자를 입력받은 후 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수

     ```python
     divmod(7, 3)
     
     # (2, 1) 출력
     ```

  7. `enumerate()` 

     - `enumerate`는 "열거하다"라는 뜻으로 순서가 잇는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 `enumerate` 객체를 돌려줌
     - 보통 `enumerate` 함수는 `for문`과 함께 자주 사용

     ```python
     for i, name in enumerate(['body', 'foo', 'bar']):
         print(i, name)
         
     '''
     <출력문>
     0 body
     1 foo
     2 bar
     '''
     ```

  8. `eval()`

     - `eval(expression)`은 실행 가능한 문자열(1 + 2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수

     ```python
     a = '1 + 2'
     print(a)	# 1 + 2 출력
     
     eval('1 + 2')	# 3 출력
     ```

  9. `filter()`

     - filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미
     - 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받음
     - 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려줌
     - `filter()` 함수 예제 (filter 사용 전)

     ```python
     # 필터링하는 함수
     def positive(l):
         result = []
         for i in l:
             if i > 0:
                 result.append(i)
         return result
     
     print(positive([1, -3, 2, 0, -5, 6]))
     # [1, 2, 6] 출력
     ```

     - `filter()` 함수 예제(filter 사용)

     ```python
     def positive(x):
         return x> 0
     
     print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
     # [1, 2, 6] 출력
     ```

     - `filter()` 함수 예제(filter)- 람다함수

     ```python
     print(list(filter(lambda x : x >0, [1, -3, 2, 0, -5, 6])))
     ```

  10. `int()`