def find_max(person):       # 최대값을 구하기 위한 함수
    max_person = person[0]  # 리스트 첫 값을 최대값으로 기본 설정
    for i in range(1, len(person)): # 처음 값은 비교할 필요가 없으므로 1부터 반복문시작
        if max_person <= person[i]:
            max_person = person[i]  # 비교후 max값 변경

    return max_person   # max값을 반환


pas_sub = []    # 각 정류장 시점의 인원을 넣기위한 리스트
total_passenger = 0 # 인원수 계산을 위한 변수

for i in range(4):
    passenger = list(map(int, input().split())) # 내린 승객과 탄 승객을 입력 받음
    
    diff =  passenger[1] - passenger[0] # 내린 승객과 탄 승객의 차이를 총 인원에 합산하기 위해 diff 변수에 넣어줌
    total_passenger += diff     # 그 시점 총 승객수 구함

    pas_sub.append(total_passenger)     # pas_sub 리스트에 값을 넣어줌


print(find_max(pas_sub))    # 위에 만든 함수에 각 정거장 기준 총 인원수를 넣은 리스트를 넣어서 최대값 출력해줌


