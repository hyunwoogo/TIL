# 셉스꺼 보고 수정

import sys
from collections import deque

N = int(input())

main_sequence = deque(sys.stdin.readline().split())
main_sequence_rev = deque(reversed(main_sequence))
sub_sequence = deque(sys.stdin.readline().split())

puzzle = False

for i in range(N):
    if main_sequence == sub_sequence or main_sequence_rev == sub_sequence:
        print('good puzzle')
        break
    main_sequence.rotate()
    main_sequence_rev.rotate()

else:
    print('bad puzzle')


# ============================================================================
# 시간초과

import sys
from collections import deque

N = int(input())

main_sequence = deque(sys.stdin.readline().split())
sub_sequence = deque(sys.stdin.readline().split())

conf_lst = []

for i in range(N):
    main_sequence.rotate()
    conf_lst.append(main_sequence)
    main_sequence.reverse()
    conf_lst.append(main_sequence)

if sub_sequence in conf_lst:
    print('good puzzle')
else:
    print('bad puzzle')


# ============================================================================
# 시간초과
import sys
from collections import deque

N = int(input())
puzzle = False

sequence = deque(sys.stdin.readline().split())
sub_sequence = deque(sys.stdin.readline().split())

for i in range(N):
    if sequence == sub_sequence or reversed(sequence) == sub_sequence:
        puzzle = True
        break
    else:
        a = sequence.popleft()
        sequence.append(a)

if puzzle == True:
    print("good puzzle")
else:
    print("bad puzzle")


# ============================================================================
# 소스 코드 인터넷 참조
# 배열의 요소가 동일한 수는 없다
# 668ms

import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
compare = list(map(int, input().split()))

# 순방향
first_idx = compare.index(sequence[0])  # 기준점
new_list1 = compare[first_idx:] + compare[:first_idx]

# 역방향
compare = compare[::-1]
first_idx = compare.index(sequence[0])  # 기준점
new_list2 = compare[first_idx:] + compare[:first_idx]

# 둘 중 하나 맞으면 good puzzle
if sequence == new_list1 or sequence == new_list2:
    print("good puzzle")
else:
    print("bad puzzle")





