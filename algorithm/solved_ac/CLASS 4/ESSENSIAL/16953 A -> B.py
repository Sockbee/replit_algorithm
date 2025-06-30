import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int, input().rstrip().split())

#2를 곱한다, 1을 가장 오른쪽 수에 추가한다.

q = deque()
mem = dict()

q.append(A)
mem[A] = 1

while q:
    x = q.popleft()
    if x == B:
        break

    for nx in [10 * x + 1, 2 * x]:
        if nx > B:
            continue

        mem[nx] = mem[x] + 1
        q.append(nx)

if B in mem:
    print(mem[B])
else:
    print(-1)