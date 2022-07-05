# 시간초과

N = int(input())

lst = []

for i in range(N):
    num = int(input())
    if num == 0:
        if lst:
            a = min(lst)
            print(a)
            lst.remove(a)
        else:
            print(0)
    else:
        lst.append(num)

# ==================================================

# 시간 초과

N = int(input())

lst = []


for i in range(N):
    num = int(input())
    if num == 0:
        if lst:
            a = lst.pop()
            print(a)
        else:
            print(0)

    else:
        lst.append(num)
        lst = sorted(lst, reverse=True)


# ==================================================
# 시간 초과
from queue import PriorityQueue

N = int(input())
que = PriorityQueue()

for i in range(N):
    num = int(input())
    if num == 0:
        if que.empty():
            print(0)
            
        else:
            a = que.get()
            print(a)
            
    else:
        que.put(num)

# ======================================================
# 시간 초과

import heapq

N = int(input())
heap = []

for i in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, num)

# ======================================================

import heapq
import sys

N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, num)





