# 나누기말고 역순으로 곱해가면서 target으로 맞춰보기
# 실패

target = int(input())
num = 1
cnt = 0
   
while target > num:
    if num * 3 <= target:
        num = num * 3
        cnt += 1
    elif num * 2 <= target:
        num = num * 2
        cnt += 1
    else:
        num += 1
        cnt += 1

print(cnt)

# ==========================================
# 나누기 and 곱하기 두개 다 해서 비교해서 작은값으로 출력
# 실패

target = int(input())


def mult():
    global target
    num = 1
    cnt = 0
    while target > num:
        if num * 3 <= target:
            num = num * 3
            cnt += 1
        elif num * 2 <= target:
            num = num * 2
            cnt += 1
        else:
            num += 1
            cnt += 1
    return cnt

def div():
    global target
    cnt = 0
    while target > 1:
        if target % 3 == 0:
            target = target // 3
            cnt += 1
        elif target % 2 == 0:
            target = target // 2
            cnt += 1
        else:
            target -= 1
            cnt += 1
    return cnt

print(min(mult(), div()))

# ==========================================
# 블로그 참고
# 피보나치처럼 작은수의 최소값을 저장 해 둔 다음 그 최소값들을 더해서 구하는방법


n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])