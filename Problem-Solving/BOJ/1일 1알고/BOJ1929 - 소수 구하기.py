# 시간초과
# import sys

# input = sys.stdin.readline
# ans_lst = []

# m, n = map(int, input().split())

# for i in range(m, n+1):
#     for j in range(2, i):
#         cnt = 0
#         if i % j == 0:
#             cnt += 1
#             break

#     if cnt == 0:
#         ans_lst.append(i)

# for i in ans_lst:
#     print(i)


# ===========================================
# 에라토스토네스의 체
# 출력 초과
# 연구 해봐야할듯
'''
에라토스테네스의 체는 가장 먼저 소수를 판별할 범위만큼 배열을 할당하여, 해당하는 값을 넣어주고, 이후에 하나씩 지워나가는 방법을 이용한다.

1. 배열을 생성하여 초기화한다.
2. 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.(지울 때 자기자신은 지우지 않고, 이미 지워진 수는 건너뛴다.)
3. 2부터 시작하여 남아있는 수를 모두 출력한다.
'''
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

lst = [i for i in range(n+1)]

for i in range(2, n+1):
    if lst[i] == 0:
        continue
    else:
        j = i * 2
        while j < (n + 1):
            if lst[j] != 0:
                lst[j] = 0
                # print(j)
                j += i

for i in range(m):
    if lst[i] != 0:
        lst[i] = 0

for i in lst:
    if i == 0:
        continue
    else:
        print(i)


# ===========================================
# 블로그 풀이
# 제곱근까지만 소수인지 구하면 알 수 있음
# 5684ms 시간 너무 오래걸림

import sys

input = sys.stdin.readline

m, n=map(int,input().split())

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break  
    else:
        print(i)