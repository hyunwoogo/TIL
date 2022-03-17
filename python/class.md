# 클래스

### 객체

- 파이썬에서 `객체(object)`라는 단위로 메모리 위의 정보를 관리
- 일단 메모리에 올라간다면 `객체`가 된다.

```python
a = 123
print(a)
print(id(a))	# 객체 주소 출력
```



### 클래스

- `클래스` 는 `객체(object)`를 표현하기 위한 문법
- `클래스` 는 `객체` 들의 집합이라고 생각하면 된다
- `클래스` 에서 정의한 `객체`를 **` 인스턴스 `** 라고 함
- `클래스` 에서 정의한 `함수`를 **` 메서드 `** 라고 함
- 클래스 사용 이유
  - 코드가 짧아진다.
  - 클래스를 사용하여 객체를 만들 경우 서로의 객체에 영향을 미치지 않음

- `클래스` 사용 이유 예제(클래스 사용 전)

```python
# 클래스 사용 전
result = 0

def add(num):
    global result
    result = num + result
    return result
print(add(3))	# 3출력
print(add(4))	# 7출력

result2 = 0
def add2(num):
    global result2
    result2 = num + result2
    return result2
print(add2(3))	# 3출력
```

> - 더하기 계산이 필요할 때마다 새로운 함수를 생성해야 함

- `클래스` 사용 이유 예제

```python
class Calculator:
    def __init__(self):		# 생성자
        self.result = 0
        
    def add(self, num):
        self.result = num + self.result
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(id(cal1))	# cal1 주소값 출력
print(id(cal1))	# cal2 주소값 출력

'''
<출력문>
1409252942320
1409252945056
'''

print(cal1.add(4))	# 3출력
print(cal1.add(3))	# 7출력

```

- `클래스` 생성 예제

```python
class Cookie:
    pass		# 빈 클래스 생성

a = Cookie()	# a에서 Cookie클래스 호출
b = Cookie()	# b에서 Cookie클래스 호출
print(type(a))	# <class '__main__.Cookie'> 출력
```



- 사칙연산 클래스 만들기 예제

```python
class FourCal:
    pass		# 일단 내용을 넣지 않고 빈 클래스를 만든 것
```

> - 빈 클래스 생성 후 어떤 용도로 사용하고 어떤 코드를 넣을 것인지 생각해보는 것이 좋음
> - `pass` 를 쓰지 않고 끝내 버리면 오류가 날 수 있음

```python
class FourCal:
    def setdata(self, first, second):	# 클래스 내의 메서드 생성
        self.first = first		# 매개변수로 받은 'first'를 self.first로 넣어줌
        self.second = second	# 매개변수로 받은 'second'를 self.second로 넣어줌
      
```

> - 클래스 내에 매서드에서 첫 매개변수는 무조건 **`'self'`** 가 들어가줌
> -  **`'self'`**  말고 다른 단어를 써도 되지만 보편적으로  **`'self'`** 를 쓴다. (일종의 약속이라 생각)

```python
a = FourCal()
a.setdata(4, 2)				# 4 == 매개변수 first == self.first == a.first
							# 2 == 매개변수 second == self.second == a.second

b = FourCal()
FourCal.setdata(b, 7, 5)	# 7 == 매개변수 first == self.first == b.first
							# 5 == 매개변수 second == self.second == b.second

# a와 b모두 클래스를 호출 하였는데 매개변수 self는 자기자신을 의미하기 때문에 굳이 안 써줘도 된다
# 저절로 클래스를 호출한 변수가 self가 되는것
# a는 self매개변수를 입력안한것이고  b는 한것
```

- 사칙연산 클래스에 더하기 기능 추가하기

```python
class FourCal:
    def setdata(self, first, second):	
        self.first = first		
        self.second = second	
        
    def add(self):
        result = self.first + self.second	# 매개변수 두개의 합을 result에 넣음
        return result		# result를 반환
```

- 사칙연산 클래스에 곱하기, 빼기, 나누기 기능 추가하기

```python
class FourCal:
    def setdata(self, first, second):	
        self.first = first		
        self.second = second	
        
    def add(self):
        result = self.first + self.second	
        return result
    
    def mul(self):		# 곱하기 메서드 정의
        result = self.first * self.second	# 매개변수 두개의 곱을 result에 넣음
        return result	# result를 반환
    
    def sub(self):		# 곱하기 메서드 정의
        result = self.first - self.second	# 매개변수 두개의 차를 result에 넣음
        return result	# result를 반환
    
    def div(self):		# 나누기 메서드 정의
        result = self.first - self.second	# 매개변수 두개를 나눈 값을 result에 넣음
        return result	# result를 반환
```

```python
a = FourCal()
a.setdata(4, 2)

print(a.add())	# 6
print(a.mul())	# 8
print(a.sub())	# 2
print(a.mul())	# 2.0
```

- **`생성자 ( Constructor ) `**

  - 인스턴스 객체가 생서될 때 초기화를 위해 자동으로 호출되는 초기화 메서드(`__init__`)
  - 파이썬 메서드 이름으로  **`__init__`** 을 사용하면 이 메서드는 생성자가 됨
  - 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기 보다는 생성자를 구현하는 것이 안전하다.
  - **`__init__`** 메서드는 인스턴스를 생성하는 순간 바로 실행이 된다.

  - 생성자 예제

  ```python
  class test:
      def __init__(self, first, second):
          self.first = first
          self.second = second
          
  a = test(4, 2)	# 생성자를 써주면 클래스 호출을 할 때 바로 매개변수를 써서 호출 가능
  ```

  ```python
  class Calculator:
      def __init__(self):		# 생성자 메서드
          self.result = 1		# 생성자에 의해 result값이 1로 자동으로 저장
          
      def add(self, num):		# 매개변수 num을 받아 쓰는 메서드
          self.result = num + self.result		# 자동으로 생성된 result(= 1)에 다가 num을 더해 result로 다시 넘겨줌 
          return self.result	# 계산한 result값 반환
      
  a = Calculator()
  ```

- **`상속`**

  - 정의
    - 부모 클래스의 모든 속성(데이터, 메서드)를 자식 클래스로 물려줌
    - 클래스의 공통된 속성을 부모 클래스에 정의
    - 하위 클래스에서는 특화된 메서드와 데이터를 정의

  - 장점
    - 각 클래스마다 동일한 코드가 작성되는 것을 방지
    - 부모 클래스에 공통된 속성을 두어 코드의 유지보수가 용이
    - 각 개별 클래스에 특화된 기능을 공통된 인터페이스로 접근 가능
  - 상속 예제

  ```python
  class FourCal:
      def setdata(self, first, second):
          self.first = first
          self.second = second
      
      def add(self):
          result = self.first + self.second
          return result
      
      def mul(self):
          result = self.first * self.second
          return result
      
      def sub(self):
          result = self.first - self.second
          return result
      
      def div(self):
          result = self.first / self.second
          return result
  ```

  ```python
  class MoreFourCal(FourCal):
      pass
  ```

  > - `FourCal`이 부모 클래스이고 `MoreFourCal`이 자식 클래스
  > - 클래스 정의 할때 ()안에 상속받을 클래스명 적어 주면 됨

  ```python
  a = MoreFourCal()
  a.setdata(4, 2)
  print(a.add())	# 부모 클래스의 add메서드를 사용
  ```

  > - 상속에 상속도 가능하다

  ```python
  class MoreFourCal2(MoreFourCal):
      pass
  
  a = MoreFourCal2()
  a.setdata(4, 2)
  print(a.add())
  ```

  - 자식 클래스에 기능이 추가 되어도 부모 클래스에 영향을 미치지 않는다.
  - 자식 클래스에 부모 클래스 메서드와 동일하게 존재하는 경우 부모 클래스의 메서드를 사용하는 것이 아닌 자식 클래스의 메서드를 사용함( `메서드 오버라이딩` )

- **`메서드 오버라이딩`**

  - 메서드 덮어쓰기 or 메서드 재정의
  - 메서드 오버라이딩 예제

  ```python
  class FourCal:
      def setdata(self, first, second):
          self.first = first
          self.second = second
      
      def add(self):
          result = self.first + self.second
          return result
      
      def mul(self):
          result = self.first * self.second
          return result
      
      def sub(self):
          result = self.first - self.second
          return result
      
      def div(self):
          result = self.first / self.second
          return result
  ```

  ```python
  a = FourCal()
  a.setdata(4, 0)
  print(a.div())	# 에러 발생, 0으로 나누어야 되기 때문에 ZeroDivisionError 발생한다.
  ```

  ```python
  class SafeFourCal(FourCal):
      def div(self):		# div메서드 재정의
          if self.second == 0:	# 2번째 매개변수가 0이면
              return 0		# 0으로 반환
          else:
              return self.first / self.second
  ```

  ```python
  a = SafeFourCal()
  a.setdata(4, 0)
  print(a.div())	# 0출력
  ```

  
