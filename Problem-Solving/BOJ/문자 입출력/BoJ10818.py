count = int(input())		# 몇개의 숫자를 넣을 건지 input으로 받음
nums = list(map(int, input().split()))	# input으로 받은 숫자를 int형으로 바꿔 리스트로 변환후 nums에 넣어줌 
if len(nums) != count:	# 만약에 count로 받은 숫자와 nums리스트안에 요소 숫자가 다르다면 프로그램 종료
    print("수가 맞지 않습니다. 다시 실행 해 주세요")
    break   
else:    # input으로 받은 숫자와 nums의 요소 개수가 같다면
    print(min(nums), end=" ")		# nums의 최소값 출력 후 한줄에 표현하기 위해 end = " " 씀
    print(max(nums))	# 최소값 바로 뒤에 nums의 최대값 나옴
