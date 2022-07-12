# 실패 
# 무조건 틀린 부분 찾아 낸다...

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

def searching(start, N):
    global cnt
    cnt += 1
    if cnt > len(graph)-1:
        return 0
    else:
        if (graph[start][0] == N):
            return cnt
        else:
            new_start = graph[start][0]
            searching(new_start, N)

for i in range(T):
    cnt = 0
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for j in range(N):
        target = int(input())
        graph[j+1].append(target)
    print(searching(1, N))

# ==================================================================
# 블로그 풀이

import sys
input = sys.stdin.readline

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        v = int(input())
        graph[i].append(v)
    check = [0]*(N+1)
    dfs(1)
    print(check[N] if check[N] > 0 else 0)



