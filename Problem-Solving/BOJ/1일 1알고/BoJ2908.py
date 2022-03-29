numbers = input()   # 비교할 숫자를 입력받음

S_numbers = numbers[len(numbers) :  : -1]   # 입력받은것이 str이기 때문에 2개의 숫자를 뒤집기위해 str자체를 뒤집어줌

S_list = S_numbers.split()      # 공백으로 나누어서 리스트로 넣음

if S_list[1] >= S_list[0]:  # 첫 번째 수 보다 두 번째 수가 더 크면 첫 번째 수 출력
    print(S_list[1])
else:                       # 아니면 두 번째 수 출력
    print(S_list[0])