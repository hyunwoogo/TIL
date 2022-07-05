# 나이는 숫자가 적어야지 많은것 처음에 min, max 변수 바꿔서 적음
# 68ms

import sys

student_lst = []

N = int(input())
for i in range(N):
    student = list(sys.stdin.readline().split())
    student_lst.append(student)     # 이차원 리스트로 명단을 만듬

min = student_lst[0]    # 비교할 대상으로 첫번째 사람 이름과 생년월일 넣음
for i in range(1, len(student_lst) - 1):    # 두번째 사람부터 비교시작
    if int(min[3]) < int(student_lst[i][3]):    # 3번자리가 연도이므로 연도가 더 크면 더 나이가 적음
        min = student_lst[i]                    # 나이가 작으면 min에 넣어줌
    elif int(min[3]) == int(student_lst[i][3]): # 연도같으면
        if int(min[2]) < int(student_lst[i][2]):    # 월 비교 월 더 큰 사람이 min으로 들어감
            min = student_lst[i]
        elif int(min[2]) == int(student_lst[i][2]):     # 월도 같으면 일 비교
            if int(min[1]) < int(student_lst[i][1]):    # 일 숫자가 더 큰 사람이 min에 들어감
                min = student_lst[i]

max = student_lst[0]                        # min의 반대로 생각 하면됨
for i in range(1, len(student_lst) - 1):
    if int(max[3]) > int(student_lst[i][3]):
        max = student_lst[i]
    elif int(max[3]) == int(student_lst[i][3]):
        if int(max[2]) > int(student_lst[i][2]):
            max = student_lst[i]
        elif int(max[2]) == int(student_lst[i][2]):
            if int(max[1]) > int(student_lst[i][1]):
                max = student_lst[i]
    

print(min[0])   # 이름 자리 출력
print(max[0])

