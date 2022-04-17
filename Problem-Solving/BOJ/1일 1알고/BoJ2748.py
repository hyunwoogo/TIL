def Fibonacci(num):
    a, b = 0, 1     # 0번째 1번째 숫자는 지정해둠
    result = 0
    if num == 0:    # 입력값이 0이면 0번째 숫자를 뜻 result는 0
        result = 0
    if num == 1:    # # 입력값이 1이면 1번째 숫자를 뜻 result는 1
        result = 1
    else: 
        for i in range(num-1):      # num-1을 하는 이유는 앞에서 num이 1일때를 지정해 줬기 때문
            c = a + b               # (n-2) + (n-1)을 더해 c에 더해줌
            result = c              # 그 결과를 result에 할당
            a = b                   # 새로운 n-2를 할당
            b = c                   # 새로운 n-1를 할당

    return result                   # result값으로 return


nums = int(input())
print(Fibonacci(nums))