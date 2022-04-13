row, col = map(int, input().split())
castle = []
count_r = 0
count_c = 0
lst = []

for i in range(row):
    security = input()
    security_lst = [security[j] for j in range(col)]
    castle.append(security_lst)

for k in range(row):
    if "X" not in castle[k]:
        count_r += 1

for _ in range(col):
    for n in range(row):
        lst.append(castle[n][_])
    if "X" not in lst:
        count_c += 1
    lst = []

answer = max(count_r, count_c)

print(answer)