# ver.1
# 시간초과

num_count = int(input())
nums = list(map(int, input().split()))
target_num = int(input())
count = 0

for i in nums:
    want_num =  target_num - i
    if want_num in nums:
        count += 1 

count = int(count / 2)      # 순서쌍이 뒤집혀서 두번씩 나오기 때문에 나누기 2를 해줌

print(count)



# ----------------------------------------------------------------------------
# ver.2
# 시간초과
import sys

num_count = int(input())
nums = list(map(int, sys.stdin.readline().split()))     # 한줄 전체를 input받을때는 sys모듈에 stdin.readline을 쓰는 것이 시간적으로 효율적
target_num = int(input())
count = 0

for i in nums:
    want_num =  target_num - i
    if want_num in nums:
        nums.remove(i)              # 마지막에 순서쌍이 두번나오는 것을 방지 하기 위해 remove를 해줌
        nums.remove(want_num)
        count += 1 

print(count)


# ----------------------------------------------------------------------------
# ver.3
# 시간초과

import sys

num_count = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
target_num = int(sys.stdin.readline())
count = 0

for i in nums:
    want_num =  target_num - i
    if want_num in nums:
        nums.remove(i)                  
        nums.remove(want_num)
        count += 1 

print(count)

# ----------------------------------------------------------------------------
# ver.4
# 시간초과

import sys

count = 0
data = []
for i in range(3):
    data.append(list(map(int,sys.stdin.readline().split())))

target_num = data[2][0]         # 2차원 리스트도 사용해봄

for j in data[1]:
    if (target_num - j) in data[1]:
        count += 1

count = int(count / 2 ) 

print(count)

# ----------------------------------------------------------------------------
# ver.5
# 시간초과
import sys 

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
target_num = int(sys.stdin.readline())
count = 0

nums.sort()
num_sub_1 = nums[:N//2]     # in으로 좀 덜 돌려고 sort 하고 앞뒤 리스트의 합으로 구해 보려고 해봄
num_sub_2 = nums[N//2:]

for i in num_sub_1:
    if (target_num - i) in num_sub_2:
        count += 1

print(count)

# ----------------------------------------------------------------------------

# 결국 답 찾아봄...
# 근데 이해 안됨...
# 예외가 있지 않을까?
# 코드 다시 보니 이해 됨

import sys

n = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

answer = 0
left, right = 0, n-1
while left < right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)


# 알고리즘 무조건 공부하기
