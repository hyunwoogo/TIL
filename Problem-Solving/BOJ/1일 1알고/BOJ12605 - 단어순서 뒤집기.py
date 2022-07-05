# 64ms
import sys

N = int(input())

for i in range(N):
    case = sys.stdin.readline().split()
    case = case[::-1]
    print(f"Case #{i+1}:", *case)
