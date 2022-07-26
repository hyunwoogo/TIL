# 마지막 예제 안됨
# 크기 비교를 어떻게 구현할 지 모르겠음

# import sys
# input = sys.stdin.readline
# days = []
# incomes = []

# def answer(N, days, incomes):
#     i = 0
#     total = 0
#     while i <= len(days) - 1:
#         total += incomes[i]
#         i += days[i]
#         if (i > N):
#             break
#         elif (i == len(days)-1) and (days[i] > 1):
#             break
   
#     return total

# N = int(input())
# for i in range(N):
#     day, income = map(int, input().split())
#     days.append(day)
#     incomes.append(income)

# print(answer(N, days, incomes))

# ===============================================
# 블로그 풀이

import sys
input = sys.stdin.readline

n = int(input())
t,p = [],[]
dp = [0] * (n+1)

for i in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

M = 0

for i in range(n):
    M = max(M,dp[i])  
    if i+t[i] > n :  
        continue
    dp[i+t[i]] = max(M+p[i],dp[i+t[i]])
print(max(dp))