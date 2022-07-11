import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

row, col = map(int, input().split())
graph = []

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < col) and (0 <= ny < row):
            if graph[ny][nx] == "#":
                graph[ny][nx] = "."
                dfs(nx, ny)


for i in range(row):
    graph.append(list(input().rstrip()))


cnt = 0
for j in range(col):
    for k in range(row):
        if graph[k][j] == "#":
            dfs(j, k)
            cnt += 1

print(cnt)