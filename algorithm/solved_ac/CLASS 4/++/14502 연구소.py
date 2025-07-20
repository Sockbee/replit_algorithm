import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph_copied):
    q = deque()
    cnt = 0
    for vi in virus:
        q.append(vi)

    while q:
        x, y  = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph_copied[nx][ny] == 0:
                    cnt += 1
                    graph_copied[nx][ny] = 1
                    q.append((nx, ny))


N, M = map(int, input().split()) # N은 세로 , M은 가로

graph = [[] for _ in range(N)]
for i in range(M):
    lst = list(map(int, input().split()))
    graph[i] = lst

#바이러스 주소들 저장
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))

for combi in combinations(N * M, 3):
    a, b, c = combi
    graph[a // M][a % M] = 1
    graph[b // M][b % M] = 1
    graph[c // M][c % M] = 1
    bfs()