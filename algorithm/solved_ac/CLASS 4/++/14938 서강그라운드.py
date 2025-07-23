import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, R = map(int, input().split()) #N은 지역의 개수, 예은이의 수색 범위 M, 길의 개수 R

items = list(map(int, input().split())) # 각 구역에 있는 아이템 수

#2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    graph[a][a] = 0

for i in range(R):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] <= M:
            result[i] += items[j - 1]

print(max(result))