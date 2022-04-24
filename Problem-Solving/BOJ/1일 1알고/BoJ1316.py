# 런타임 에러

nums = int(input())
str_lst = []
count = 0

for i in range(nums):
    group_voc = list(input())
    if len(group_voc) <= 2:
        continue
    else:
        for j in group_voc:
            if group_voc.count(j) <= 1:
                continue
            else:
                number = group_voc.count(j)
                for k in range(number):
                    first = group_voc.index(j, k)
                    second = group_voc.index(j, k+1)
                    if second - first >= 2:
                        count += 1
                        break
                    
                break

answer = nums - count

print(answer)

# -------------------------------------------------------------------------------
#  요셉님꺼 보고 수정

N = int(input())
count = 0

for i in range(N):
    voc = input()
    for j in range(len(voc)):
        if voc.find(voc[j], j+1, len(voc)) - j > 1:
            count += 1
            break

print(N - count)

