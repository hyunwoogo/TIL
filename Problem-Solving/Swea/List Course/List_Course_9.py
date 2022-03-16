T = int(input())     # 테스트 횟수를 입력

for t in range(T):  # 테스트 횟수 만큼 반복
    N, M = map(int, input().split())    # 몇개의 숫자와 부분합을 몇개씩 할 것인지 설정
    nums = list(map(int, input().split()))  # 숫자셋 입력
    max_num = sum(nums[0 : M])  # 제일 묶음으로 부분합 최대값 기본 설정
    min_num = sum(nums[0 : M])  # 제일 묶음으로 부분합 최대값 기본 설정
    
    for i in range(N - M + 1):  
        if max_num < sum(nums[i : i + M]):  # 최대값 비교
            max_num = sum(nums[i : i + M])  #  더 크면 max에 넣어줌
        elif min_num > sum(nums[i : i + M]): # 최소 비교
            min_num = sum(nums[i : i + M])  # 더 작으면 min에 넣어줌

        
    answer = max_num - min_num  # max - min을 answer 변수에 저장
    print(f"#{t+1} {answer}")


