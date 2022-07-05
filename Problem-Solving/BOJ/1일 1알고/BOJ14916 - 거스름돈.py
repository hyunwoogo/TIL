# "BOJ2839 - 설탕배달"과 같은 개념
# 68ms

won = int(input())
won_num = 0

while won > 0:
    if won % 5 == 0:
        won_num += won // 5
        break
    won -= 2
    won_num += 1

if won < 0:
    print(-1)
else:
    print(won_num)
