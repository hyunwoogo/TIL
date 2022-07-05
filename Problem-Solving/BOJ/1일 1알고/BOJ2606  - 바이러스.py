# 실패
# import sys

# N = int(sys.stdin.readline())
# edge_num = int(sys.stdin.readline())

# lst = []
# sub_lst = []


# for i in range(edge_num):
#     a, b = map(int, sys.stdin.readline().split())
#     if i == 0:
#         fir_a = a
#         fir_b = b
#         if fir_a == 1 or fir_b == 1:
#             lst.append(fir_a)
#             lst.append(fir_b)
#         else:
#             sub_lst.append(fir_a)
#             sub_lst.append(fir_b)
#     else:
#         if a in lst or b in lst:
#             lst.append(a)
#             lst.append(b)
#         elif a == 1 or b == 1:
#             lst.append(a)
#             lst.append(b)
#         else:
#             sub_lst.append(a)
#             sub_lst.append(b)

# for k in range(len(sub_lst)):
#     if sub_lst[k] in lst:
#         if k % 2 == 0:
#             lst.append(sub_lst[k])
#             lst.append(sub_lst[k+1])
#         else:
#             lst.append(sub_lst[k-1])
#             lst.append(sub_lst[k])


# num_set = set(lst)
# print(len(num_set) - 1)

# ===========================================================================================

import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

mat = [[0]*(V+1) for i in range(V+1)]

for i in range(E):
    start, end = map(int, sys.stdin.readline().split())
    mat[start][end] = 1
    mat[end][start] = 1

# 나중에 다시 풀어보기