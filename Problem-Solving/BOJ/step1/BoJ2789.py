word = list(input().upper())   # 단어를 입력받아 upper로 대문자 변환 후 리스트화
del_word = "CAMBRIDGE"   # "CAMBRIDGE"에 속하는 단어를 지우기위해 비교하려고 변수에 저장

for i in range(len(word)):   
    if word[i] in del_word:   # 리스트에 있는것이 del_word에 들어 있다면
        word[i] = ""    # 그 리스트 요소의 내용을 없애줌
    else:
        print(word[i], end = '')   # 나머지 요소들을 줄바꿈을 안하고 아닌 계속 이어 써줌