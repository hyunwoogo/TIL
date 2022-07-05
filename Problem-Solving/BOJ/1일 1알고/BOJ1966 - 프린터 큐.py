import sys
from collections import deque


N = int(input())

for i in range(N):
    count = 0
    n, m = list(map(int, sys.stdin.readline().split()))
    doc_imp = deque(sys.stdin.readline().split())
    idx_lst = list(range(len(doc_imp)))
    target = doc_imp[m]
    while True:
        if doc_imp[0] == max(doc_imp):
            count += 1
            
            if doc_imp[0] == target:
                print(count)
                break
            else:
                doc_imp.popleft()
            
        else:
            doc_imp.rotate(-1)
            


        





