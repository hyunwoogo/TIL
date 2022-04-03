nums = int(input())         # 받을 숫자 개수
num = [int(input()) for i in range(nums)]       # 받은 숫자를 리스트로 만듬
num_1 = 0       # 2개의 숫자 비교를 위해 변수 2개 만듬
num_2 = 0        

for i in range(nums):       # 받은 숫자 개수 만큼 반복문 돌림
    for j in range(nums-1): # j번째 수와 j + 1번째 수를 비교하기 위해 nums - 1만큼 반복 돌림
        num_1 = num[j]      
        num_2 = num[j+1]
        if num_1 > num_2:   # num_1이 num_2보다 크다면
            num[j] = num_2
            num[j+1] = num_1    # 위치를 바꿔줌
        else:
            continue        # 아니라면 다시 반복문 수행


for _ in num:
    print(_)