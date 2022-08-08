# 108ms
# 시간 더 줄이는 방법 생각해봐야겠다

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0

que = deque([i for i in range(1, n+1)])
lst = list(map(int, input().split()))

for i in range(len(lst)):
    cnt_left = 0
    cnt_right = 0
    if lst[i] == que[0]:
        que.popleft()
    else:
        while lst[i] != que[0]:
            que.rotate(-1)
            cnt_left += 1
        for j in range(cnt_left):
            que.rotate(1)
        while lst[i] != que[0]:
            que.rotate(1)
            cnt_right += 1
        que.popleft()
    cnt += min(cnt_left, cnt_right)

print(cnt)