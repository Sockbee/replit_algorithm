import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(0, n + 1)]

for i in range(m):
  a, b = list(map(int, input().rstrip().split()))
  graph[a].append(b)
  graph[b].append(a) # 양방향 그래프

visited = set()
queue = deque([1])
visited.add(1)

while queue:
  node = queue.popleft()

  for neighbor in graph[node]:
    if neighbor not in visited:
      visited.add(neighbor)
      queue.append(neighbor)

#print(graph)
print(len(visited) - 1)