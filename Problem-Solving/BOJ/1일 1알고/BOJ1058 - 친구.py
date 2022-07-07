# 실패
import sys
sys.setrecursionlimit(100000)

N = int(input())
graph = []
sub_visited = []
visited = []
ans_lst = []

def dfs(n):
    global sub_visited
    for i in range(len(graph)):
        if (graph[n][i] == "Y") and (i not in sub_visited):
            sub_visited.append(i)
            dfs(i)
        
        visited.append(sub_visited)
        sub_visited = []

    return len(visited)

for i in range(N):
    row = list(input())
    graph.append(row)

for j in range(N):
    result = dfs(j)
    ans_lst.append(result)
    print(ans_lst)
    visited = []
    

# ==============================================================================
# 실패
import sys
from collections import deque

N = int(input())
graph = []
fri_lst = []

def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        a = queue.popleft()
        for i in range(len(graph[start])):
            if (graph[a][i] == "Y") and (i not in visited):
                visited.append(i)
                queue.append(i)

    return len(visited) - 1

for i in range(N):
    row = list(sys.stdin.readline().rstrip())
    graph.append(row)


for j in range(N):
    pre_ans = bfs(j)
    fri_lst.append(pre_ans)

print(max(fri_lst))

# ============================================================================
# 블로그 참고
# 아직 3중 for문을 왜 써야되는지 이해가 안감

import sys
input = sys.stdin.readline
n = int(input())
s = []
visit = [[0] * n for i in range(n)]
def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if s[i][j] == "Y" or (s[i][k] == "Y" and s[k][j] == "Y"):
                    visit[i][j] = 1
for i in range(n):
    s.append(list(input().strip()))
floyd()
result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visit[i][j] == 1:
            cnt += 1
    result = max(result, cnt)
print(result)