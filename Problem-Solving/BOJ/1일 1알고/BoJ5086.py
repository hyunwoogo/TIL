answer = []     # 정답 받아줄 리스트 생성

while True:     # 무한루프
    A, B = map(int, input().split())        # 수 두개 받음
    if A == 0 and B == 0:                   # 맨 마지막줄에는 0 0이 들어가므로 그 수를 만나면 반복문 멈춤
        break
    else:                                   # 배수 약수 따져 보고 결과값 answer 리스트에 넣음
        if B % A == 0:
            answer.append("factor")
        elif A % B == 0:
            answer.append("multiple")
        else:
            answer.append("neither")


print(*answer, sep = "\n")      # 리스트 출력