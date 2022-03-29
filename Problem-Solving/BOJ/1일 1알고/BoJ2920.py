ascend_num = [i for i in range(1, 9)]   # ascending을 출력하기 위해 비교 리스트 생성
descend_num = [j for j in range(8, 0, -1)]  # descending을 출력하기 위해 비교 리스트 생성

nums = list(map(int, input().split()))      # 내용을 입력받음

if nums == ascend_num:  # ascend_num과 같으면 "ascending" 출력
    print("ascending")
elif nums == descend_num:   # descend_num과 같으면 "descending" 출력
    print("descending")
else:                   # 두 가지 경우가 아니면 "mixed" 출력
    print("mixed")