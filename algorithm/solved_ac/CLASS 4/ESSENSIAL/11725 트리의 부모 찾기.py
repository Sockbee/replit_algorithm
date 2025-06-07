import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)
visited = [False] * (N + 1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                visited[neighbor] = True
                q.append(neighbor)

bfs(1)

for i in range(2, N + 1):
    print(parent[i])