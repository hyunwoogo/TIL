# 파일 입출력

### 1. `open`

- 파일 생성하기 예제

```python
f = open('새파일.txt', 'w')
f.close()
```

> - `open` 함수는 다음과 같이 '파일 이름'과 '파일 열기 모드'를 입력값으로 받고 결과값으로 파일 객체를 돌려줌
>
> - 파일객체 = open(파일 이름, 파일 열기 모드)
>
> - 파일 열기 모드 종류
>
>   - `r(읽기모드)` - 파일을 읽기만 할 때 사용
>   - `w(쓰기모드)` - 파일의 내용을 쓸 때 사용
>   - `a(추가모드)` - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
>
>   ※ 쓰기모드로 열게 되면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성

- 파일 생성 후 내용 넣기 예제

```python
f = open('새파일.txt', 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)	# 파일에 data라는 내용을 써주겠다
f.close()	# 파일 객체를 닫아주는 역할 생략가능 하지만 다시 파일을 사용하려면 무조건 닫아주기
			# 안닫고 다음에 쓰려고 하면 충돌 발생
```

- 폴더가 없을 경우 폴더를 생성하면서 파일을 만드는 방법

```python
import os	# 폴더 생성을 위해 os모듈 import

out_dir = "새폴더"
if out_dir not in os.listdir():		# 디렉토리 목록에 '새폴더'가 존재 안하면 만들어 줌
    os.mkdir(out_dir)
    
f = open("새폴더/새파일.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```



- 파일 첫번째 줄 읽기( `readline()` )

```python
f = open('새파일.txt', 'r')
line = f.readline()
print(line)		# "1번째 줄입니다." 출력
print(type(line))	# <class 'str'> 출력
f.close()
```

- 파일의 모든 내용 읽기 예제 1

```python
f = open('새파일.txt', 'r')
while True:
    line = f.readline()
    if not line:	# 읽어올 라인이 없으면 break문으로 반복문 끝내기
        break
    print(line)
f.close()

'''
<출력문>
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
'''
```

> - `readline()` 은 더 이상 읽을 라인이 없을 경우 `None` 을 출력

- 파일의 모든 내용 읽기 예제 2 (`readlines()`)

```python
f = open('새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

'''
<출력문>
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
'''
```

> - readline() 함수는 호출될 때 파일에서 한 줄을 반환
> - readlines() 함수는 호출될 때 각 요소가 파일의 한줄인 리스트 형식으로 파일의 모든 줄을 반환

```python
f = open('새파일.txt', 'r')
lines = f.readlines()
print(lines)
# ['1번째 줄입니다. \n', '2번째 줄입니다. \n', '3번째 줄입니다. \n', '4번째 줄입니다. \n', '5번째 줄입니다. \n', '6번째 줄입니다. \n', '7번째 줄입니다. \n', '8번째 줄입니다. \n', '9번째 줄입니다. \n', '10번째 줄입니다. \n'] 출력
print(type(lines))	# <class 'list'> 출력
```

- 파일의 모든 내용 읽기 예제 3 (`read()` )

```python
f = open('새파일.txt', 'r')
data = f.read()
print(data)
print(type(data))
f.close()

'''
<출력문>
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
<class 'str'>
'''
```

>- readline() : 파일의 한 줄 관련 함수
>  - 한 줄 읽고 나서 포인터가 다음 줄로 이동
>- readlines() : 파일 내용 전체를 가져와 리스트로 반환
>  - 각 줄은 문자열 형태로 리스트의 요소로 저장
>- read() : 파일 내용 전체를 하나의 문자열로 반환



- 파일 내용 추가하기 예제(write)

```python
f = open('새파일.txt', 'a')	# '새파일'에 다음줄 부터 이어 쓰기 위해 'a(추가모드)'로 파일 열기 
for i in range(11, 20):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()
```

```python
f = open('새파일.txt', 'r')
data = f.read()
print(data)
f.close()

'''
<출력문>
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
11번째 줄입니다.
12번째 줄입니다.
13번째 줄입니다.
14번째 줄입니다.
15번째 줄입니다.
16번째 줄입니다.
17번째 줄입니다.
18번째 줄입니다.
19번째 줄입니다.
20번째 줄입니다.
'''
```

---



### 2. `with open`

- `open`과 다르게 파일을 닫아 줄 필요 X( 자동으로  close가 되기 때문 )
- 파일 생성하기 예제

```python
with open('foo.txt', 'w') as f:		# 'as f'는 오픈한 파일을 f라고 지칭하겠다는 의미
    f.write("Life is too short, you nee python")
```

```python
with open('foo.txt', 'r') as f:
    data = f.read()
    print(data)		# "Life is too short, you need python" 출력
```

- 파일 라인 지우기 예제

```python
with open('새파일.txt', 'r') as f:
    data = f.read()
    print(data)
    
'''
<출력문>
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
11번째 줄입니다.
12번째 줄입니다.
13번째 줄입니다.
14번째 줄입니다.
15번째 줄입니다.
16번째 줄입니다.
17번째 줄입니다.
18번째 줄입니다.
19번째 줄입니다.
20번째 줄입니다.
'''
```

```python
f = open('새파일.txt', 'r')
lines = f.readlines()
f.close()

del lines[10:]

new_file = open('새파일_변경.txt', 'w')

for line in lines:
    new_file.write(line)
    
new_file.close()
```

```python
with open('새파일_변경.txt', 'r') as f:
    data = f.read()
    print(data)
    
'''
<출력문>
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
'''
```

> - 파일 입출력에서는 지운다는 개념이 존재X
> - 읽어와서 리스트에서 지운 후 새로운 파일을 생성하는것

