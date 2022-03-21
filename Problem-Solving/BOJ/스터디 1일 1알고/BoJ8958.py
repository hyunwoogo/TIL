test = int(input())     # 테스트 할 횟수 입력받음

for i in range(test):
    quiz_result = input()   # 퀴즈의 결과를 받음
    result = len(quiz_result)   # 퀴즈의 결과 만큼 반복문을 돌리기 위해 변수 설정
    count = 0   # 연속으로 맞추는 경우 하나씩 숫자를 올리기 위해 변수 생성
    sum = 0     # 총 점수 계산을 위한 변수 생성
    for j in range(result):
        if quiz_result[j] == "O":   
            count += 1      # 맞췄을 경우 count를 1 올려줌
            sum += count    # count의 결과를 sum에 더해줌
        elif quiz_result[j] == "X":
            count = 0       # 못 맞췄을 경우 다시 count를 0으로 초기화

    print(sum)