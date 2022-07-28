# 어캐 구현할까...

import sys
input = sys.stdin.readline

row, col = map(int, input().split())
A = []
B = []


for i in range(row):
    A.append(list(map(int, input().rstrip())))

for i in range(row):
    B.append(list(map(int, input().rstrip())))

print(A)
print(B)


# ===================================================
# 블로그 보고 문제를 잘 못 이해했다는 걸 암

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for j in range(N)]
B = [list(map(int, input().rstrip())) for j in range(N)]
cnt = 0


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]


for i in range(N - 2):  # 줄바꿈 가능 횟수
    for j in range(M - 2):  # 가로 줄 이동 가능 횟수
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

        if A == B:
            break
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(cnt)