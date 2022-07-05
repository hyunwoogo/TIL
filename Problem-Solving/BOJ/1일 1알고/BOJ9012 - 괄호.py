# 76ms
import sys

N = int(input())

for i in range(N):
    brackets = sys.stdin.readline().rstrip()
    bracket_lst = []

    for j in range(len(brackets)):
        if len(bracket_lst) == 0:
            bracket_lst.append(brackets[j])
        else:
            if bracket_lst[-1] == '(' and brackets[j] == ')':
                bracket_lst.pop()
            else:
                bracket_lst.append(brackets[j])

        # print(bracket_lst)

    if bracket_lst:
        print('NO')
    else:
        print("YES")