count = int(input())
nums = list(map(int, input().split()))
if len(nums) != count:
    print("수가 맞지 않습니다. 다시 실행 해 주세요")
else:
    print(min(nums), end=" ")
    print(max(nums))