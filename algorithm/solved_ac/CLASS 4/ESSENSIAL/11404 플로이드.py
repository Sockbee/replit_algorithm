import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    graph[a][a] = 0

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N + 1):
    for b in range(1, N + 1):
        #도달할 수 없는 경우 0이라고 출력
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = ' ')
    print()