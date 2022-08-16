# 시간초과
import sys
input = sys.stdin.readline

def prime_num(number):
    flag = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            flag = False
            break
    return flag

def answer(n):
    ans_lst = []
    for i in range(1, int(n/2) +1):
        if prime_num(i) and prime_num(n - i):
            cand_ans = [i, n-i]
            ans_lst.append(cand_ans)

    return ans_lst[-1]

N = int(input())

for i in range(N):
    num = int(input())
    print(*answer(num))