import sys
input = sys.stdin.readline
from collections import deque

graph = []
lst_P = []
is_founded = False
start_my_x = 0
start_my_y = 0
n, m = list(map(int, input().rstrip().split()))

for i in range(n):
    lst = input().rstrip()
    graph.append(lst)
    for j in range(m):
        if lst[j] == 'P':
            lst_P.append((i, j))
        if not is_founded and lst[j] == 'I':
            start_my_y = j
            start_my_x = i

visited = [[0] * m for _ in range(n)]

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

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 'X' or visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = 1

bfs(start_my_x, start_my_y)

ans = 0
for p in lst_P:
    x, y = p
    if visited[x][y]:
        ans += 1

if ans:
    print(ans)
else:
    print("TT")