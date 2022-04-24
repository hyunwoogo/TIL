# 실패
# 전체 중 3가지를 뽑는 조합의 수에다가 겹치는 부분을 빼고 안되는 조합을 모두 뺌
# 런타임 에러 (RecursionError)
# 백준 재귀 깊이 1000

def Factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * Factorial(n-1)

def Combination(n, m):
    result = int(Factorial(n) / (Factorial(m) * Factorial(n - m)))
    return result



overlab_cnt = 0
bad_lst = []

N, M = map(int, input().split())

for i in range(M):

    first, second = map(int, input().split())
    bad_lst.append(first)
    bad_lst.append(second)

for j in range(N):
    if bad_lst.count(j+1) > 1:
        overlab_cnt += bad_lst.count(j+1) - 1



total_num = Combination(N, M)
bad_num = int((Combination(N-2, 1) * (len(bad_lst) / 2) ) - overlab_cnt)
answer = total_num - bad_num

print(answer)


# -----------------------------------------------------------------------
# 런타임 에러 (TypeError)

def Factorial(n):
    result = 1
    if n == 1:
        return result
    elif n > 1:
        for i in range(n, 1, -1):
            result *= i
        return int(result)

def Combination(n, m):
    result = int(Factorial(n) / (Factorial(m) * Factorial(n - m)))
    return result

overlab_cnt = 0
bad_lst = []

N, M = map(int, input().split())

for i in range(M):
    first, second = map(int, input().split())
    bad_lst.append(first)
    bad_lst.append(second)

for j in range(N):
    if bad_lst.count(j+1) > 1:
        overlab_cnt += bad_lst.count(j+1) - 1

total_num = Combination(N, M)
bad_num = int((Combination(N-2, 1) * (len(bad_lst) / 2) ) - overlab_cnt)
answer = total_num - bad_num

print(answer)

