import sys
from collections import deque
input = sys.stdin.readline
#print = sys.stdout.write

graph = []
m, n = list(map(int, input().rstrip().split()))
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

# 상하좌우 이동을 위한 델타값
dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽

days = [[-1] * m for _ in range(n)]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = 0
    days[start_x][start_y] = 0
    

    while queue:
        x, y = queue.popleft()
        #print(f"방문: ({x}, {y})")

        for i in range(4):  # 네 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 갈 수 없거나 이미 방문한 곳 무시
            if graph[nx][ny] == -1 or visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            if days[nx][ny] != -1:
                days[nx][ny] = min(days[nx][ny], days[x][y] + 1)
            else:
                days[nx][ny] = days[x][y] + 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            #print("bfs", i, j)
            bfs(i, j)

_max = -2
flag = 0
for i in range(n):
    for j in range(m):
        if days[i][j] == -1 and graph[i][j] == 0:
            print("-1")
            flag = 1
            break
        else:
            _max = max(_max, days[i][j])
    if(flag == 1):
        break
if not flag:
    print(_max)