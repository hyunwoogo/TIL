nums = int(input())     # 받을 숫자 개수
num = [int(input()) for i in range(nums)]   # 받은 숫자를 리스트로 만듬
sort_num = []       # 정렬시키기 위해 새로운 리스트를 만듬

for i in range(nums):       # 받은 숫자 갯수 만큼 반복문 돌림 
    min_num = min(num)      # 받은 숫자 중 제일 최소값 저장하는 변수로 저장
    min_idx = num.index(min_num)    # 최소값 인덱스 값도 변수로 저장
    sort_num.append(min_num)    # 새로운 리스트에 최소값을 넣어줌
    num.pop(min_idx)            # 최소값을 기존 리스트에서 제외 시켜줌

for _ in sort_num:      # 출력
    print(_)
