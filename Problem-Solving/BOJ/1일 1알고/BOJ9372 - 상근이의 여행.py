# 실패
# import sys

# T = int(sys.stdin.readline())

# for i in range(T):
#     cnt = 0
#     nation, airplane = map(int, sys.stdin.readline().split())
#     nation_set = set(range(1, nation+1))
#     nation_sub_set = set()
#     for i in range(airplane):
#         a, b = map(int, sys.stdin.readline().split())
#         if a not in nation_sub_set and b not in nation_sub_set:
#             nation_sub_set.add(a)
#             nation_sub_set.add(b)
#             cnt += 1
#         elif a not in nation_sub_set and b in nation_sub_set:
#             nation_sub_set.add(a)
#             cnt += 1
#         elif a in nation_sub_set and b not in nation_sub_set:
#             nation_sub_set.add(b)
#             cnt += 1
#         else:
#             break
    
#     print(cnt)

# ==========================================================================================
# 1096ms(너무 오래 걸림)

import sys

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

T = int(sys.stdin.readline())

for i in range(T):
    dic = {}
    visited = []
    nation, airplane = map(int, sys.stdin.readline().split())
    for i in range(nation):
        dic[i+1] = set()
    for j in range(airplane):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].add(b)
        dic[b].add(a)

    dfs(1, dic)
    print(len(visited)-1)



# ==========================================================================================
# 인터넷 참고 (184ms)
# 너무 쉽게 풀려 당황쓰...

import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 수

for _ in range(T) :
    N, M = map(int, sys.stdin.readline().split()) 

    for _ in range(M) :
        a, b = map(int, sys.stdin.readline().split())
    print(N-1)
