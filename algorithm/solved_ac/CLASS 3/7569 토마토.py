import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().rstrip().split()) # M은 가로 수, N은 세로 수

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

days = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque()

graph = []
for i in range(H):
    floor = []
    for j in range(N):
        lst = input().rstrip().split()
        floor.append(lst)
    graph.append(floor)

# 모든 익은 토마토(1)를 BFS 시작 지점으로 추가
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == '1':
                queue.append((i, j, k))
                days[i][j][k] = 0  # 시작 지점은 0일차

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if graph[nz][ny][nx] == '0' and days[nz][ny][nx] == -1:
                days[nz][ny][nx] = days[z][y][x] + 1
                queue.append((nz, ny, nx))

max_day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == '0' and days[i][j][k] == -1:
                print(-1)
                sys.exit()
            max_day = max(max_day, days[i][j][k])

print(max_day)