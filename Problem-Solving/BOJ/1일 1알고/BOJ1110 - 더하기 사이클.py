# 실행이 안됨...
# N = int(input())

# cycle_num = 0

# while True:
    
#     cycle_num += 1

#     if N < 10:
#         new_N = (N * 10) + N
#         if new_N == N:
#             break

#     else:
#         a = N // 10
#         b = N % 10
#         new_num = a + b
#         new_N = (b * 10) + (new_num % 10)
#         if new_N == N:
#             break


# print(cycle_num)


# =====================================================

# number = int(input())

# cycle_num = 0
# while True:
#     cycle_num += 1

#     if number < 10:
#         new_number = (number * 10) + number
#         if new_number == number:
#             break
#     else:
#         ten = number // 10
#         one = number % 10
#         ten_one = ten + one
#         new_number = (one * 10) + (ten_one % 10)
#         if new_number == number:
#             break

# print(cycle_num)

# =======================================================

# 변수 설정 때문에 시간이 걸림
# if로 10보다 작은수를 나눌 필요가 없던 것을 깨달음
number = int(input())

cycle_num = 0

new_number = number     # whlie문 안에서 계속 변하면서 돌 수 있게 new_number변수 정해줌

while True:

    a = new_number      # 계산식에 필요하게 한번 더 변수 정해줌
    cycle_num += 1      # 몇바퀴 돈지 수
    ten = a // 10       # 10의 자리
    one = a % 10        # 1의 자리
    ten_one = ten + one     # 두개 더한거
    new_number = (one * 10) + (ten_one % 10)    # 새로운 수 만들어냄
    if new_number == number:        # 새로 만들어진 수가 처음 input받았던 수와 같으면 break
        break

print(cycle_num)