# 아이디어는 떠오르는데 예외도 있을거 같고 구현을 못하겠음....연습이 아직 많이 필요
# N = int(input())
# graph = []
# ans_mat = [[0]*N for i in range(N)]
# idx_lst = []

# def dfs(start, graph):
#     for i in range(len(graph[start])):
#         if graph[start][i] == 1:
#             idx_lst.append(i)



# for i in range(N):
#     graph.append(list(map(int, input().split())))

# ==============================================================================
# 블로그 코드1(DFS만 이용)

n = int(input())
visit = [0 for i in range(n)]
s = []
def dfs(v):
    for i in range(n):
        if visit[i] == 0 and s[v][i] == 1:
            visit[i] = 1
            dfs(i)

for i in range(n):
    s.append(list(map(int, input().split())))

for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visit = [0 for i in range(n)]


# ==============================================================================
# 블로그 코드2(플로이드-워셜 알고리즘 이용)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
    
# 플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()
 
'''

요약하자면 i를 출발해 j로 바로 가는 것보다

i를 출발해 k를 거쳐 j로 가는 게 효율적일 경우(저렴할 경우) 해당 값을 갱신해주는 것이다.

경로 k라 해서 하나의 정점 k만 거치는 것이 아니다. 여러 정점을 거치는 모든 경우의 수가 포함되어 있다.

'''

