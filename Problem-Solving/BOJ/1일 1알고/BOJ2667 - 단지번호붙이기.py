# 내가 푼거 계속 오류남...솔직히 상하좌우 이동 개념을 아직 잘 모르겟음
# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline

# def dfs(x, y):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < N) and (0 <= ny < N):
#             if graph[ny][nx] == 1:
#                 graph[ny][nx] = -1
#                 cnt += 1
#                 dfs(nx, ny)
#             else:
#                 group_lst.append(cnt)


# N = int(input())
# cnt = 0

# graph = [[0]*N for i in range(N)]

# sub_graph = []
# group_lst = []

# for j in range(N):
#     line = input().split()
#     sub_graph.append(line)

# for i in range(N):
#     for j in range(N):
#         graph[i][j] = int(sub_graph[i][0][j])


# list(map(int, input())) 쓰면 숫자 다 분리 된다는거 몰랐음;;

# ====================================================================
# 블로그 코드1(보고나서 조금 이해가 됨)
# indexerror..?
# N = int(input())

# graph = []  # 집(그래프) 나타낼 리스트

# cnt = 0     # 현재 탐색 중인 단지의 집의 수
# house = []  # 단지별 개수 저장

# # 집 입력받기
# for i in range(N):
#     graph.append(list(map(int, input())))

# # 상하좌우 한칸씩 이동
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# # DFS 방법
# def dfs(x, y):
#     global cnt

#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         cnt += 1    # 집을 하나 카운트 해줬으니 +1

#         # 상하좌우 좌표 이동
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 범위 check
#             if (0 <= nx <= N) and (0 <= ny <= N):
#                 # dfs를 재귀로 수행
#                 dfs(nx, ny)

#     else:
#         return

# # 이중 for문을 통해 graph 순회
# for x in range(N):
#     for y in range(N):

#         # 1로 표시되어 있다면 DFS 수행
#         if graph[x][y] == 1:
#             dfs(x, y)

#             house.append(cnt)   # 단지 단위의 순회가 끝났으므로 house에 추가
#             cnt = 0     # 다음 단지 카운트를 위해 0으로 리셋

# print(len(house))

# house.sort()    # 오름차순

# for h in house:
#     print(h)

# ====================================================================
# 블로그 코드 2
# indexerror..?
# size = int(input())
# address = [] # 집의 유무 (1,0)을 저장
# visited = [[0 for _ in range(size)] for _ in range(size)] # 방문 기록 저장
# answer =[] #  단지 내 집 수 저장
# counter = 0 # 단지 갯수 저장

# for i in range(size):
#     address.append(list(map(int, input())))

# def DFS(row,col):
#     if (visited[row][col] == 0): # 만약 집이 방문된 적 없다면
#         visited[row][col] += 1 # 방문기록 추가
#         if (address[row][col] == 1): # 만약 집이 존재한다면 (1)
#             answer[counter] +=1 # 현재 단지 번호에 해당하는 집 수 1 증가
#             if (row>0): # 왼쪽 이동 가능여부
#                 if (visited[row-1][col]==0):
#                     DFS(row-1,col)     
#             if (col>0): # 위쪽 이동 가능 여부
#                 if (visited[row][col-1]==0):
#                     DFS(row,col-1)
#             if (row<size-1): # 우측 이동 가능 여부
#                 if (visited[row+1][col]==0):
#                     DFS(row+1,col)     
#             if (col<size-1): # 아래쪽 이동 가능 여부
#                 if (visited[row][col+1]==0):
#                     DFS(row,col+1)

# for i in range(size): 
#     for j in range(size): # 모든 집을 순회하면서 
#         if (visited[i][j] == 0 and address[i][j] == 1): # 집을 방문한 적 없고, 집이 존재한다면
#             answer.append(0) # 단지 내 집 수
#             counter += 1 # 단지 수
#         DFS(i,j) # 깊이 우선탐색

# print(counter+1)
# answer.sort() # 정렬
# for i in range(len(answer)):
#     print(answer[i])

# ====================================================================
# 블로그 코드3
# 76ms

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def Dfs(cur_x, cur_y, visited, house_count):
    visited[cur_x][cur_y] = True
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        if next_x <= -1 or next_x >= n or next_y <= -1 or next_y >= n:
            continue
        if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
            house_count = Dfs(next_x, next_y, visited, house_count + 1)

    return house_count

answer_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            answer_list.append(Dfs(i, j, visited, 1))

answer_list.sort()

print(len(answer_list))
for i in answer_list:
    print(i)