# 100ms

from collections import deque
import sys

N = int(input())
queue = deque()

for i in range(N):
    cmd_lst = list(sys.stdin.readline().split())

    if cmd_lst[0] == 'push':
        queue.append(cmd_lst[1])

    elif cmd_lst[0] == 'pop':
        if len(queue) != 0:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    
    elif cmd_lst[0] == 'size':
        print(len(queue))

    elif cmd_lst[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd_lst[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    
    elif cmd_lst[0] == 'back':
        if len(queue) != 0:
            print(queue[len(queue)-1])
        else:
            print(-1)
        



