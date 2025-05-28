import sys
input = sys.stdin.readline
from collections import defaultdict as dd

T = int(input().rstrip())

for _ in range(T):
    M, N, x, y = list(map(int, input().rstrip().split()))
    a, b = 0, 0
    
    dd_dict = dd()
    cnt = 0
    while a < M or b < N:
        if a < M:
            a = a + 1
        else:
            a = 1

        if b < N:
            b = b + 1
        else:
            b = 1
        
        cnt = cnt + 1
        dd_dict[(a, b)] = cnt
    if (x, y) in dd_dict:
        print(dd_dict[(x, y)])
    else:
        print('-1')