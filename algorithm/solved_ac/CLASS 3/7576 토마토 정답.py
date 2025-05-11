import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

days = [[-1] * m for _ in range(n)]
queue = deque()

# 모든 익은 토마토(1)를 BFS 시작 지점으로 추가
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            days[i][j] = 0  # 시작 지점은 0일차

# BFS 실행
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and days[nx][ny] == -1:
                days[nx][ny] = days[x][y] + 1
                queue.append((nx, ny))

# 결과 계산
max_day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and days[i][j] == -1:
            print(-1)
            sys.exit()
        max_day = max(max_day, days[i][j])

print(max_day)