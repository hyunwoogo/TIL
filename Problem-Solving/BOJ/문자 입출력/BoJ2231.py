def union_fun(num):         # 각 자리수 더 할 함수 정의
    num_sum = 0             # 각 자리수 합을 넣어줄 변수 정의
    while num:
        n = num % 10        # n에는 매개변수로 받은 수의 1의 자리를 넣음
        num = num // 10     # num은 10으로 나눈 몫을 넣어줌
        num_sum += n        # n의 값을 num_sum에 계속 넣어줌
                            # 위 코드를 반복 돌리면 자리수가 점점 줄어들면서 각 자리수 더하기 가능
    return num_sum          # 함수를 num_sum값으로 반환

N = int(input())

for i in range(1, 1000000):     # 출력값이 가장 작은 생성자를 구하는 것이기 때문에 1부터 시작
    temp = union_fun(i)         # 각자리수를 더한 함수를 temp변수에 넣어줌
    if i + temp == N:           # 생성자 조건 부합 하면
        print(i)                # 출력
        break                   # 반복문 멈춤

else:                           # 반복문이 안 멈추면 0 출력
    print(0)