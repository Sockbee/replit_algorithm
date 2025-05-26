import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip().split())

graph = []
for _ in range(N):
    graph.append(input().rstrip())

visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == '0' or visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

bfs(0, 0)

print(visited[N - 1][M - 1])