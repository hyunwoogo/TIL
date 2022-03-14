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
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result = num + self.result
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

