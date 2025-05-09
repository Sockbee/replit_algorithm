import sys
from collections import deque
input = sys.stdin.readline

visited = set()

def bfs(graph, start):
  queue = deque([start])
  visited.add(start)

  while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)


N, M = list(map(int, input().rstrip().split()))

graph1 = [[] for _ in range(0, N + 1)]
all_node = deque(range(1, N + 1))

for i in range(M):
  a, b = list(map(int, input().rstrip().split()))
  graph1[a].append(b)
  graph1[b].append(a)

cnt = 0
while all_node:
  bfs(graph1, all_node[0])
  cnt += 1
  all_node = deque(set(all_node) - visited)

print(cnt)