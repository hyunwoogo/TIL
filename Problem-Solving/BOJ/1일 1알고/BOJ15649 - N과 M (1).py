# 블로그 참고
# 이해가 안됨 (백트래킹의 개념, 밑에 코드도 어떻게 다 돌 수 있는지)
# -> 요셉스 설명으로 이해 완료
# 백트래킹: DFS일종 (차이점은 가지를 칠 수 있느냐)

n, m = map(int, input().split())

s = []
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    f()
    s.pop()

f()