# idea: 층마다 리스트 만들어서 2중 리스트 만든 다음 계속 더해가면서 마지막
# 리스트에서 최댓값 구하면 됨
# 312ms

from copy import deepcopy
import sys
input = sys.stdin.readline

tri = []
n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    tri.append(line)

sub_tri = deepcopy(tri)

for i in range(len(tri)-1):
    for j in range(len(tri[i])):
        tri[i+1][j] = max(tri[i+1][j], tri[i][j] + sub_tri[i+1][j])
        tri[i+1][j+1] = max(tri[i+1][j+1], tri[i][j] + sub_tri[i+1][j+1])

print(max(tri[-1]))