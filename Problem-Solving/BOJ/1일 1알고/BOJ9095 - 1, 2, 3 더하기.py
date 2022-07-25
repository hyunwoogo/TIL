# n = n-3 + n-2 + n-1
# 72ms

import sys
input = sys.stdin.readline
ans = []

T = int(input())

def sum_case(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return sum_case(num-3) + sum_case(num-2) + sum_case(num-1)

for i in range(T):
    num = int(input())
    a = sum_case(num)
    ans.append(a)

for j in ans:
    print(j)