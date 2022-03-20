# 예외처리

- 오류가 발생했을 때 처리 하는 것

- 오류의 종류

  1. **`FileNotFoundError`**
     - 없는 파일을 열거나 파일을 찾지 못했을 때 발생하는 에러
  2. **`ZeroDivisionError`**
     - 0으로 다른 숫자를 나누는 경우 발생하는 에러
  3. **`IndexError`**
     - 리스트나 문자열의 인덱싱 슬라이싱을 수행할때 범위가 벗어나면 발생하는 에러
  4. **`IndentationError`** 
     - 들여쓰기에 관련된 에러
  5. **`SyntacError`**
     - 따옴표의 짝이 맞지 않을때
     - in 뒤에 리스트나 enumerate() 같은 함수가 아니라 연산자가 나왔을때
  6. **`NameError`**
     - 없는 변수를 호출하거나 변수 이름이 틀린 경우
  7. **`RecursionError`**
     - 재귀함수 관련 에러 자기자신을 계속해서 호출하다가 에러 메시지를 출력하며 종료
  8. **`AttributeError`**
     - 리스트에 없는 속성을 호출
     - 모듈에 없는 속성을 호출
  9. **`ValueError`**
     - 함수 안에 실행인자를 잘못 입력한 경우
  10.  **`TypeError`**
      - 함수의 작성자가 의도하지 않은 자료형이 들어갈 경우 발생
  11. **`KeyError`**
      - 존재하지 않는 key를 호출했을 경우 에러가 발생

- **`예외`** 란?

  - 프로그램의 제어 흐름을 조정하기 위해 사용하는 이벤트
  - 오류를 무시하고 프로그램을 정상적으로 실행

- 예외 처리 기법

  1.  `try ~ except` 문

     - `try` 블록 수행 중 오류가 발생하면 `except` 블록이 수행
     - `try` 블록에서 오류가 발생하지 않는다면 `except` 블록은 수행 되지 않음
     - 예제

     ```python
     a, b = 5, 0
     try:
         c = a / b
         print(c)
     except:
         print("error")
         
         
     # "error" 출력, b가 0인데 a를 0으로 나눠서 에러 발생
     ```

     > - 오류 종류에 상관없이 오류가 발생하면 `except` 블록을 수행

     - `try ~ except` 문 (에러 지정) 예제

     ```python
     a, b = 5, 0
     try:
         c = a / b
         pritn(c)
     except ZeroDivisionError:		# ZeroDivisionError 일때만 except블록을 수행
         print("error")
     ```

     ```python
     try:
         spam()
     except NameError as x:
         print(x)		# 오류 메시지를 출력하는 것
         
     # name 'spam' is not defined 출력
     ```

     - 여러 개의 예외 발생

       - except 문을 여러번 사용 가능
       - 형식)

       ```python
       try:
           some_job()
       except ZeroDivisionError:
           <구문>
       except NameError:
           <구문>
       except (TypeError, IOError):	# 두가지 에러를 동시에 잡아냄
           <구문>
       ```

     - 두 가지의 예외를 한 번에 묶어서 처리하기 예제

     ```python
     try:
         a = [1, 2]
         print(a[3])
         4/0
     except (ZeroDivisionError, IndexError) as e:
         print(e)
         
     # list index out of range 출력
     # 4/0 보다 print(a[3])이 먼저 읽어 지기 때문에 indexerror를 먼저 감지하고 그것이 출력됨
     ```

  2.  `try ~ finally` 문

     - try, except, finally 문 세 개가 다 들어갈 수 잇음
     - try 문에서 정상 동작 중인 코드가 에러를 만날 경우
       - except 문을 수행
       - except 문 수행이 끝나면 finally 문이 수행
     - try 문에서 코드가 끝까지 정상 동작할 경우
       - try 문 수행이 끝나면 finally 문이 수행
     - finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행
     - `try ~ finally` 문 예제

     ```python
     x = 0
     try:
         print(x)
         1 / x
     except:
         print("error")
     finally:
         print("어떤 경우에도 호출이 된다")
         
     '''
     <출력문>
     0
     error
     어떤 경우에도 호출이 된다
     '''
     ```

     - 오류 회피하기 예제

     ```python
     try:
         f = open("없는 파일", 'r')
     except FileNotFoundError:
         pass
     ```

     > - 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있는데 그때에 사용

  3.  예외 만들기

     - 예제

     ```python
     class MyError(Exception):
         pass
     
     def say_nick(nick):
         if nick == "바보":
             raise MyError()
         print(nick)
         
     say_nick("바보")		# 에러(MyError) 발생
     ```

     > - raise 문을 사용하여 예외를 발생시킬 수 있음
     > - raise 뒤에 쓰여진 클래스는 예외 클래스의 인스턴스 객체처럼 받아들여짐

     - 만든 예외를 실제 코드에 적용하기 예제

     ```python
     try:
         say_nick("천사")
         say_nick("바보")
     except MyError:
         print("허용되지 않는 별명입니다.")
         
     '''
     <출력문>
     천사
     허용되지 않는 별명입니다.
     '''
     ```

     - 오류 메시지를 작성하여 출력하기 예제

     ```python
     class MyError(Exception):
         def __str__(self):
             return "허용되지 않는 별명입니다."
     
     def say_nick(nick):
         if nick == "바보":
             raise MyError()
         print(nick)
         
     say_nick("바보")
     ```

     - 출력값

     ![image-20220320213210669](C:\Users\GHW\AppData\Roaming\Typora\typora-user-images\image-20220320213210669.png)

- 번외) 에러 종류를 확인하는 코드

```python
import sys
import traceback

x = 0
try:
    1/x
except:
    etype, evalue, tb = sys.exc_info()
    print("Exception class :", etype)
    print("value :", evalue)
    print("traceback object :", tb)
    print("="*10)
    traceback.print_exc()
```

- 출력값

![image-20220320213508280](C:\Users\GHW\AppData\Roaming\Typora\typora-user-images\image-20220320213508280.png)