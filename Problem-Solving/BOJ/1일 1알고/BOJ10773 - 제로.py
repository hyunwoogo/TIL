numbers = int(input())  # 몇개의 숫자 받을건지 리스트

rest_num = []   # 숫자들 넣을 리스트

for i in range(numbers):
    a = int(input())    
    if a == 0:      
        rest_num.pop()  # 받은 숫자가 0이면 바로 직전에 들어갔던 숫자 빼기
    else:
        rest_num.append(a)  # 0이 아니면 리스트에 넣기

print(sum(rest_num))    # 리스트 합 구함