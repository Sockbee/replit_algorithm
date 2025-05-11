import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

graph = []
n, m = list(map(int, input().rstrip().split()))
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

#n = len(graph)       # 행
#m = len(graph[0])    # 열

# 방문 여부 확인용 배열
visited = [[-1] * m for _ in range(n)]

# 상하좌우 이동을 위한 델타값
dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 0

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
            if graph[nx][ny] == 0 or visited[nx][ny] != -1:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            # (i, j)부터 탐색 시작
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            if (graph[i][j] == 1):
                print("-1 ")
            else:
                print("0 ")
        else:
            print(str(visited[i][j]) + ' ')
    print('\n')