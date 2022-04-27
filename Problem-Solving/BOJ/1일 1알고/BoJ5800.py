import sys

N = int(input())    # class 갯수 입력받음

gap_lst = []        # 학생들 점수 차를 받기 위한 리스트

for i in range(N):  
    class_lst = list(map(int, sys.stdin.readline().split()))    # 클래스의 학생수와 점수들을 받아서 리스트로 만듬
    student_num = class_lst[0]  # 학생 수 따로 빼줌
    student_score = class_lst[1:]   # 점수들만 따로 빼서 새로운 리스트 생성 
    student_score.sort()            # 숫자 오름차순으로 정렬(풀고나니 내림차순으로 하라고 했는데 오름차순으로 해도 정답ㅎ)
    for j in range(student_num-1):
        gap = student_score[j+1] - student_score[j]     # 각 구간 차이 구함
        gap_lst.append(gap)                             # gap_lst에 넣어줌
        Largest_gap = max(gap_lst)                      # 최대 차이를 Largest_gap 변수에 넣음
        

    Max = max(student_score)        # 점수 중 최대값
    Min = min(student_score)        # 점수 중 최소값
    print(f"Class {i+1}")           # format으로 다 출력
    print(f"Max {Max}, Min {Min}, Largest gap {Largest_gap}")
    gap_lst = []        # 다음 class를 위해 리스트 비워줌