english = [chr(i) for i in range(97, 123)]  # 'a'부터 'z'까지를 가지는 리스트를 생성, 아스키 코드로 97부터 122까지 a ~ z 

word = input()  # 단어 입력받음

for i in english:   # 'a'에서 'z'까지 반복문돌림
    if i in word:   # 만약에 그 스펠링이 단어 안에 있으면
        print(word.find(i), end = " ")  # 단어에 그 스펠링이 몇번째 있는지 출력
    else:
        print(word.find(i), end = ' ')    # 없다면 -1 출력
