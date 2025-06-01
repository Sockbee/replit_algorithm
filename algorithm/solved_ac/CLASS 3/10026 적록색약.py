import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())

graph = []
for i in range(n):
    graph.append(input().rstrip())

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
pairs = { (i, j) for i in range(n) for j in range(n) }

cnt = 0
while pairs:
    cnt += 1
    py, px = pairs.pop()
    visited[py][px] = True
    queue.append((py, px))
    current = graph[py][px]
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if visited[ny][nx] == False and graph[ny][nx] == current:
                visited[ny][nx] = True
                pairs.remove((ny, nx))
                queue.append((ny, nx))

print(cnt, end = ' ')

visited = [[False] * n for _ in range(n)]
pairs = { (i, j) for i in range(n) for j in range(n) }

cnt = 0
while pairs:
    cnt += 1
    py, px = pairs.pop()
    visited[py][px] = True
    queue.append((py, px))
    current = graph[py][px]
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if visited[ny][nx] == False:
                if graph[y][x] != 'B' and graph[ny][nx] != 'B':
                    visited[ny][nx] = True
                    pairs.remove((ny, nx))
                    queue.append((ny, nx))
                elif graph[y][x] == 'B' and graph[ny][nx] == 'B':
                    visited[ny][nx] = True
                    pairs.remove((ny, nx))
                    queue.append((ny, nx))
print(cnt)