# 제어문

### 1. if문

- 프로그래에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰이는 것이  `if문`

- if가 참일 경우 수행될 문장은 `들여쓰기(tab)`를 하거나 `4칸` 을 띄운다(`if블록`).

  - 들여쓰기와 스페이스로 띄우는 것을 혼합해서 쓰면 에러가 날 수도 있으니 주의!!

- `if문` 기본구조

  ![image-20220312144511770](control_statement.assets/image-20220312144511770.png)

- 조건문을 테스트 해서 참이면 `if문` 바로 다음의 문장(if 블록)들을 수행

- 조건문이 거짓이면 else문 다음의 문장(else블록)들을 수행

- else문은 if문 없이 독립적으로 사용 불가

- `if문`  예제

```python
money = True
if money:	# money가 True기 때문에 if 문 실행
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
# "택시를 타고 가라" 출력
```

- pass

  - 조건문을 판단하고 참 거짓에 따라 행동을 정의 할 때 아무런 일도 하지 않게끔 설정할때 사용 

  - pass문 사용 예제

  ```python
  pocket = ['paper', 'money', 'cellphone']
  if 'money' in pocket:
      pass
  else:
      print("카드를 꺼내라")
      
  # pass로 인해 아무것도 출력하지 않음
  ```

- elif

  - if와 else만으로는 다양한 조건을 판단하기 어려운 경우가 발생
  - 다양한 조건을 만들기 위해 사용
  - elif  구조

  ![image-20220312145156906](control_statement.assets/image-20220312145156906.png)

  - elif 구문 예제

  ```python
  # 1. elif를 사용 X
  pocket = ['paper', 'card', 'cellphone']
  if 'money' in pocket:
      print("택시를 타고 가라")
  else:
      if card:
          print("택시를 타고 가라")
      else:
          print("걸어가라")
          
          
  # 1. elif를 사용
  pocket = ['paper', 'card', 'cellphone']
  if 'money' in pocket:
      print("택시를 타고 가라")
  elif card:
      print("택시를 타고 가라")
  else:
      print("걸어가라")
  ```



- 한 줄 if문 예제

```python
pocket = ['paper', 'money', 'celphone']
if 'money' in pocker: pass
else: print("카드를 꺼내라")	
# pass로 인해서 출력 X
```



---

### 2. while 문

- 반복해서 문장을 수행해야 할 경우 while문을 사용
- `while(조건문)` 에서 조건문이 False 될 때까지 반복
- `while문` 기본구조

![image-20220312151308903](control_statement.assets/image-20220312151308903.png)