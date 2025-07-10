import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int, input().split())

q = deque()
q.append(A)
distance = [-1 for _ in range(100001)]
distance[A] = 0
ways = [0 for _ in range(100001)]
ways[A] = 1

while q:
    x = q.popleft()
    
    for nx in [2 * x, x + 1, x - 1]:
        if nx < 0 or nx > 100000:
            continue
        if distance[nx] == -1:
            distance[nx] = distance[x] + 1
            ways[nx] = ways[x]
            q.append(nx)
        elif distance[nx] == distance[x] + 1:
            ways[nx] += ways[x]

print(distance[B])
print(ways[B])