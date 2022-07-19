# 2980ms...

import sys
input = sys.stdin.readline
sushi = []
ans = []

'''
N: 접시의 수
d: 초밥의 가짓수
k: 연속해서 먹는 접시의 수
c: 쿠폰번호
'''
N, d, k, c = list(map(int, input().split()))

for i in range(N):
    num = int(input())
    sushi.append(num)
   
sushi.extend(sushi)
start = 0
end = k

while True:
    sushi_set = set(sushi[start:end])
    if c not in sushi_set:
        sushi_set.add(c)
        ans.append(len(sushi_set))
        start += 1
        end += 1
    else:
        ans.append(len(sushi_set))
        start += 1
        end += 1


    if end == N + k:
        break

print(max(ans))