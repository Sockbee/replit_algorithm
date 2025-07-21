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
                    graph_copied[nx][ny] = 2 #감염띠
                    q.append((nx, ny))

    return NM - cnt - LEN_VIRUS - CNT_WALL


N, M = map(int, input().split()) # N은 세로 , M은 가로
NM = N * M

original_graph = [[] for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    original_graph[i] = lst

#바이러스 주소들 저장
#빈칸 주소들도 저장
#벽 개수도 저장
virus = []
empty = []
CNT_WALL = 0
for i in range(N):
    for j in range(M):
        if original_graph[i][j] == 0:
            empty.append((i, j))
        elif original_graph[i][j] == 2:
            virus.append((i, j))
        else:
            CNT_WALL += 1
CNT_WALL += 3 #벽 3개 골라서 추가할거니까

LEN_VIRUS = len(virus)

result = -1

for combi in combinations(empty, 3):
    a, b, c = combi
    original_graph[a[0]][a[1]] = 1
    original_graph[b[0]][b[1]] = 1
    original_graph[c[0]][c[1]] = 1

    result = max(result, bfs([row[:] for row in original_graph]))

    original_graph[a[0]][a[1]] = 0
    original_graph[b[0]][b[1]] = 0
    original_graph[c[0]][c[1]] = 0

print(result)