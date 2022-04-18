# 메모리 초과
# def BABBA(string, num):

#     A_count = 0
#     B_count = 0

#     for _ in range(num):
#         lst = list(string)
#         for i in range(len(lst)):
#             if lst[i] == "A":
#                 lst[i] = "B"
#             elif lst[i] == "B":
#                 lst[i] = "BA"

#         string = "".join(lst)

#     A_count = string.count("A")
#     B_count = string.count("B")

#     return A_count, B_count

# string = "A"
# K = int(input())
# a, b = BABBA(string, K)
# print(a, b)

# -----------------------------------------------------------------------
# 시간초과
# string = "A"
# K = int(input())
# count_A = 0
# count_B = 0

# for _ in range(K):
#     lst = list(string)
#     for i in range(len(lst)):
#         if lst[i] == "A":
#             lst[i] = "B"
#         elif lst[i] == "B":
#             lst[i] = "BA"

#         string = "".join(lst)

# count_A = string.count("A")
# count_B = len(string) - count_A

# print(count_A, count_B)

# -----------------------------------------------------------------------
#  A, B 둘다 피보나치와 같은 패턴
# 64 ms
def count_A(num):       # A에 대한 피보나치 수열 함수
    result = 0
    a, b, c = 0, 1, 0
    if num == 0:
        return result
    elif num == 1:
        return result
    elif num == 2:
        result = b
        return result
    elif num >=3:
        for i in range(num-2):
            c = a + b
            result = c
            a = b
            b = c

    return result

def count_B(num):       # B에 대한 피보나치 수열 함수
    result = 0
    a, b, c = 0, 1, 0
    if num == 0:
        result = 0
        return result
    elif num == 1:
        result = b
        return result

    elif num >=2:
        for i in range(num - 1):
            c = a + b
            result = c
            a = b
            b = c

    return result
    
K = int(input())
print(count_A(K), count_B(K))
