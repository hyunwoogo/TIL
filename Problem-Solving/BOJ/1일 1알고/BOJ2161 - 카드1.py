# 68ms

number = int(input())
nums = [i+1 for i in range(number)]
new_nums = []

while len(nums) > 1:
    trash = nums.pop(0)
    new_nums.append(trash)
    re_num = nums.pop(0)
    nums.append(re_num)

answer = new_nums + nums

for i in answer:
    print(i, end=" ")