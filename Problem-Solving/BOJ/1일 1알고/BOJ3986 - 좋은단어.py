# 도저히 문제 자체가 이해가 X 다른사람꺼 풀이
# 괄호문제라고 생각
# 선이 교차한다는것 -> 괄호의 짝이 맞지 않다

import sys
input = sys.stdin.readline
 
n = int(input())
cnt = 0
 
for _ in range(n):
    s = input().rstrip()
    stack = []
 
    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
 
    if not stack:
        cnt += 1
print(cnt)

# 조원들 풀이 보고 이해완료