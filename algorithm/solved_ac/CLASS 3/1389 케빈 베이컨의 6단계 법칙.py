import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = [INF] * (n + 1)
for i in range(1, n + 1):
    ans[i] = sum(graph[i][1:n+1])

min_index = 0
_min = ans[0]
for i in range(1, n + 1):
    if _min > ans[i]:
        _min = ans[i]
        min_index = i

print(min_index)