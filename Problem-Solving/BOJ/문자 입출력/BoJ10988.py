# 풀이를 작성해 주세요
my_str = list(input())   # 문자를 받아서 리스트로 만들어줌

new_str = []    # 받은 문자를 뒤집어서 넣을 빈 리스트 생성

count = 0    # 글자 하나하나가 다 맞는지 count를 확인 하기 위해 생성

for i in range(len(my_str)):   # 글자 길이 만큼 반복
    new_str.append(my_str[len(my_str)-1 - i])    # 입력받은 문자를 뒤에서 부터 새로운 리스트에 넣음 


for i in range(len(my_str)):    # 글자길이가 입력받은것과 뒤집은것 두개가 같기 때문에 둘중 아무거나 리스트 길이 만큼 반복
    if my_str[i] == new_str[i]:    # 입력문자와 그 문자를 뒤집은 문자를 비교
        count += 1    # 카운트 하나 올려줌
        if count == len(my_str):   # 카운트와 문자길이와 같다는 것은 문자가 다 같다는 뜻
            print("1")    # 1 출력
            break    # 종료

    else:    # count가 문자길이와 다르다면 똑같다고 볼 수 없음
        print("0")    # 0 출력
        break    # 종료