submit = []     # 제출한 학생 번호 받기 위한 리스트
non_submit = [] # 비제출 학생 번호를 넣기 위한 리스트


for i in range(28):     # 2명은 안냈으니까 28번을 돌림
    student_num = int(input())
    submit.append(student_num)  # 입력받아 하나씩 제출 리스트로 넣음

for j in range(30):     # 1 ~ 30 까지 돌면서 제출 리스트에 없으면 그 번호를 비제출 리스트로 넣음
    if (j+1) in submit:
        continue
    else:
        non_submit.append(j+1)

# 비제출리스트의 크기 비교는 j가 돌아가는 for 문에서 낮은 번호 순서대로 해서 굳이 써 줄 필요 없음

for _ in non_submit:    # 비제출 리스트 출력
    print(_)