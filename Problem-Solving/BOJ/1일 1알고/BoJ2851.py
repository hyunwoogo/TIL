mush_num = []   # 버섯 갯수 넣어줄 리스트
mush_sum1 = 0   # 버섯 갯수 합을 넣어줄 변수
mush_sum2 = 0   # 100과의 차이를 비교하기 위해 하나 더 만들어줌

for i in range(10):     # 버섯 갯수 받아서 리스트로 넣음
    mush = int(input())
    mush_num.append(mush)

for j in mush_num:      # for문을 돌려 100을 넘는 순간 마지막으로 더한 값을 더한 것과 안 더한 값을 sum1과 sum2에 각각 넣어주고 break 
    mush_sum1 += j
    mush_sum2 += j
    if mush_sum1 >= 100:
        mush_sum2 -= j
        break

if abs(100 - mush_sum1) <= abs(100 - mush_sum2):    # 100과의 차이 값이 작은 쪽을 출력
    print(mush_sum1)
else:
    print(mush_sum2) 