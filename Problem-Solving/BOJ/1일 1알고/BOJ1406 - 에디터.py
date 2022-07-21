# 시간초과

# import sys
# input = sys.stdin.readline

# voc = list(input().rstrip())
# idx = len(voc)

# N = int(input())
# for i in range(N):
#     cmd = list(input().split())
#     if cmd[0] == "P":
#         voc = voc[:idx] + list(cmd[1]) + voc[idx:]
#         idx += 1

#     elif cmd[0] == "L":
#         if idx == 0:
#             continue
#         else:
#             idx -= 1
#     elif cmd[0] == "D":
#         if idx == len(voc):
#             continue
#         else:
#             idx += 1
#     elif cmd[0] == "B":
#         if idx == 0:
#             continue
#         else:
#             voc.pop(idx-1)
#             idx -= 1

# print("".join(voc))

# ==============================================================
# 블로그
# 내가 짠 코드처럼 슬라이싱을 이용하면 시간복잡도가 더 커짐(O(N)으로)
# append, pop만 사용했을시에 시간복잡도가 O(1)이 됨

import sys

left=list(input())
right=[]
M=int(input())

for i in range(M):
    com=sys.stdin.readline().split()

    if com[0]=='L':
        if left:
            right.append(left.pop())
    elif com[0]=='D':
        if right:
            left.append(right.pop())
    elif com[0]=='B':
        if left:
            left.pop()
    elif com[0]=='P':
        left.append(com[1])

right.reverse()
for i in left+right:
    print(i,end='')