# 시간초과
# import sys

# N = int(input())

# nums = [i+1 for i in range(N + 1)]

# ticket = list(map(int, sys.stdin.readline().split()))

# for j in ticket:
#     if j in nums:
#         nums.remove(j)

# answer = min(nums)

# print(answer)

# =========================================================================
# 564ms (시간 너무 오래 걸리네....)

import sys

N = int(input())

nums = [i+1 for i in range(N)]

ticket = list(map(int, sys.stdin.readline().split()))
ticket = sorted(ticket)
idx = 0

if nums != ticket:
    while nums[idx] == ticket[idx]:
        idx += 1
    answer = nums[idx]
else:
    answer = len(nums) + 1 

print(answer)

