# 실패
import sys
from collections import deque

def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        a = queue.popleft()
        for j in range(1, len(mat[start])):
            if (mat[a][j] == 1) and (j not in visited):
                visited.append(j)
                queue.append(i)
    return visited


N = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
mat = [[0]*(N+1) for _ in range(N+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    mat[x][y] = 1
    mat[y][x] = 1

print(bfs(1))




# ====================================================================================
# 88ms

import sys
from collections import deque

input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node]+1
                queue.append(n)
       
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
bfs(s)
print(check[e] if check[e] > 0 else -1)

