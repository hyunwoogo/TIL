test_num = int(input())    # 반복할 횟수 담는 변수 생성


for i in range(1, test_num + 1):
    positive_num = int(input())
    test_case = list(map(int, input().split()))
    if len(test_case) > positive_num:    # positive_num과 입력 수를 맞추기 위해 if문 씀
        print("많은 수를 입력했습니다.") 
        continue
    elif len(test_case) > positive_num:    # positive_num과 입력 수를 맞추기 위해 if문 씀
        print("작은 수를 입력했습니다.") 
        continue
    else:    # positive_num과 일치하면 최댓값과 최솟값 차이 출력
        print(f"#{i} : {max(test_case)- min(test_case)} ")