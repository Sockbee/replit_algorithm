import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [list(map(int, input().split())) + [1] for _ in range(N)]

graph.append([1] * (N + 1))

d = [[0] * (N + 1) for _ in range(N + 1)]

p = [(0, 1), (1, 0), (1, 1)] # 가로 세로 대각선 순

q = deque([(0, 1, 0)])
d[0][1] = 1

while q:
    x, y, dir = q.popleft()
    if x == N - 1 and y == N - 1:
        break

    if dir == 0:
        if not graph[x][y + 1]:
            q.append((x, y + 1, 0))
            d[x][y + 1] += d[x][y]
            if not graph[x + 1][y] and not graph[x + 1][y + 1]:
                q.append((x + 1, y + 1, 2))
                d[x + 1][y + 1] += d[x][y]

    elif dir == 1:
        if not graph[x + 1][y]:
            q.append((x + 1, y, 1))
            d[x + 1][y] += d[x][y]
            if not graph[x][y + 1] and not graph[x + 1][y + 1]:
                q.append((x + 1, y + 1, 2))
                d[x + 1][y + 1] += d[x][y]

    elif dir == 2:
        if not graph[x][y + 1]:
            q.append((x, y + 1, 0))
            d[x][y + 1] += d[x][y]
        if not graph[x + 1][y]:
            q.append((x + 1, y, 1))
            d[x + 1][y] += d[x][y]
        if not graph[x][y + 1] and not graph[x + 1][y] and not graph[x + 1][y + 1]:
            q.append((x + 1, y + 1, 2))
            d[x + 1][y + 1] += d[x][y]

print(d)
