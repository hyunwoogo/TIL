lst = []
answer = 0

for i in range(1, 46):
    lst_sub = [i]*i
    lst += lst_sub

A, B = map(int, input().split())

for j in range(A, B+1):
    answer += lst[j-1]

print(answer)