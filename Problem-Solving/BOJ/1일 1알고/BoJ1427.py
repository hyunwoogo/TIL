num = input()
num_sort = []

for i in range(len(num)):
    num_sort.append(num[i])

num_sort.sort(reverse=True)
print(*num_sort, sep="")