# 인터넷 참고(코드도 복붙) 보면서 이해 후 코드 복붙

import sys

n, m, v = map(int, sys.stdin.readline().split())
mat = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    mat[a][b] = 1
    mat[b][a] = 1


def dfs(start, visited):
    visited += [start]
    for j in range(len(mat[start])):
        if mat[start][j] == 1 and (j not in visited):
            dfs(j, visited)

    return visited

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        a = queue.pop(0)
        for j in range(len(mat[start])):
            if mat[a][j] == 1 and (j not in visited):
                visited.append(j)
                queue.append(j)

    return visited


print(*dfs(v, []))
print(*bfs(v))


