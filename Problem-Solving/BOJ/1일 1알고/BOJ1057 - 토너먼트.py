'''
idea: n의 반틈을 기준으로 k와 h가 반대편에 있으면 n을 2로 소인수 분해 한만큼 값
      같은 쪽에 있으면 n의 반틈의 값으로 계속 실행
'''

# 예제 1, 3, 5 안됨
         
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def cal(n, k, h):
    lst = [i for i in range(1, n+1)]
    lst_first = lst[:n//2]
    lst_second = lst[n//2:]
    if ((k in lst_first) and (h in lst_first)) or ((k in lst_second) and (h in lst_second)):
        if n % 2 == 0:
            n = n // 2
            if (k % 2 != 0) and (h % 2 != 0):
                k = (k + 1) // 2
                h = (h + 1) // 2
            elif k % 2 != 0:
                k = (k + 1) // 2
                h = h // 2
            elif h % 2 != 0:
                k = k // 2
                h = (h + 1) // 2
            else:
                k = k // 2
                h = h // 2
            cal(n, k, h)
        else:
            n = (n // 2) + 1
            if (k % 2 != 0) and (h % 2 != 0):
                k = (k + 1) // 2
                h = (h + 1) // 2
            elif k % 2 != 0:
                k = (k + 1) // 2
                h = h // 2
            elif h % 2 != 0:
                k = k // 2
                h = (h + 1) // 2
            else:
                k = k // 2
                h = h // 2
            cal(n, k, h)
   
    return n


def factorization(a):
    cnt = 0
    while a != 1:
        if a % 2 == 0:
            a = a // 2
            cnt += 1
        else:
            a = (a - 1) // 2
            cnt += 1
    return cnt


n, k, h = map(int, input().split())

number = cal(n, k, h)
answer = factorization(number)
print(answer)


# 블로그 풀이

n,start,end=map(int, input().split())
cnt=0
while start!=end:
  start -= start//2
  end -= end//2
  cnt+=1
print(cnt)