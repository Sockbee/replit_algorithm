import sys
from collections import deque
input = sys.stdin.readline
import copy

# (0, 0) 부터 BFS를 실행에서 어디가 바깥 공기인지 구별

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]              

N, M = map(int, input().rstrip().split()) #N이 세로 수, M이 가로 수
graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().rstrip().split()))


def mark_air():
    visited = [[0 for i in range(M)] for j in range(N)]
    air = [[0 for i in range(M)] for j in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    air[0][0] = 1

    while q:
        x, y = q.popleft()     

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    air[nx][ny] = True
                    q.append((nx, ny))
    return air

def solve():
    time = 0
    q = deque()

    while True:
        air = mark_air()
        q.clear()

        #이번 분기에 녹을 치즈를 q에 넣기
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    #녹는 치즈인지 확인
                    cnt = 0
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if air[nx][ny]:
                            cnt += 1
                    if cnt >= 2:
                        q.append((i, j))

        if not q:
            break

        while q:
            x, y = q.popleft()
            graph[x][y] = 0
            
        time += 1

    return time

print(solve())