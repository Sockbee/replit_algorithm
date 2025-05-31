from collections import deque

# 예시 지도 (1은 길, 0은 벽)
graph = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 0]
]

n = len(graph)       # 행
m = len(graph[0])    # 열

# 방문 여부 확인용 배열
visited = [[False] * m for _ in range(n)]

# 상하좌우 이동을 위한 델타값
dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        print(f"방문: ({x}, {y})")

        for i in range(4):  # 네 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 갈 수 없거나 이미 방문한 곳 무시
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True

# (0, 0)부터 탐색 시작
bfs(0, 0)