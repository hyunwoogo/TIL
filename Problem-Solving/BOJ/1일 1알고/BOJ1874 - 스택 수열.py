# 도저히 머리가 안돌아감
# 계속 indexrange error 뜸
import sys
input = sys.stdin.readline

N = int(input())
nums = [i for i in range(N, 0, -1)]
goal = []
cal = []
ans = []
i = 0

for i in range(N):
    num = int(input())
    goal.append(num)

a = nums.pop()
cal.append(a)

while nums:
    if cal[-1] == goal[i]:
        b = cal.pop()
        ans.append(b)
        i += 1
        print("-")
       

    else:
        print("+")
        c = nums.pop()
        cal.append(c)

print(nums)

# =============================
# 블로그 풀이
# 어렵다..

n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)