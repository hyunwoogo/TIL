# idea: dfs, bfs 방식?으로 i에서 j로 가는 방법을 찾아 거리를 distance변수로 계산하여 dist 리스트에 넣음
#       이중리스트 dist에서 내부 리스트의 max값만 for문을 돌면서 새로운 리스트에 넣고 그 리스트에 max값을 답으로 출력

# import sys
# input = sys.stdin.readline

# N = int(input())
# tree = [[0] * N for i in range(N)]
# dist = [[0] * N for i in range(N)]
# distance = 0

# def route(start, end):
#     if tree[start][end] != 0:
#         dist[start][end] = tree[start][end]
#         dist[end][start] = tree[start][end]
#     else:
        

# for i in range(N-1):
#     a, b, c = map(int, input().split())
#     tree[a-1][b-1] = c
#     tree[b-1][a-1] = c

# ==============================================================================
# 블로그 참고

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))


