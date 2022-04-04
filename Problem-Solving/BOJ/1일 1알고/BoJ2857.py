lst = []    # 첩보원명 받을 리스트
lst_idx = []    # FBI가 있는 index값 받을 리스트

for i in range(5):  # 첩보원명을 입력 받아 리스트에 넣음
    names = input()
    lst.append(names)

for j in range(len(lst)):   # 리스트를 돌며 FBI가 문자열에 있는지 확인후 있으면 그 리스트 인덱스 값을 lst_idx에 넣음
    if "FBI" in lst[j]:
        lst_idx.append(j+1)

if lst_idx == []:       # 인덱스 리스트가 비어 있으면 아래 문자열 출력
    print("HE GOT AWAY!")
    
else:               # 인덱스 리스트에 내용이 있으면 하나씩 출력
    for _ in lst_idx:
        print(_, end=" ")
        
