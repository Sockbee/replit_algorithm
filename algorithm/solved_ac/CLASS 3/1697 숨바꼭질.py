import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, K = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(0, 100001)]

visited = set()
parent = {}

queue = deque([N])
visited.add(N)
parent[N] = None


flag = 0
while queue:
    node = queue.popleft()
    graph[node].append(2 * node)
    graph[node].append(node + 1)
    graph[node].append(node - 1)

    if (node == K):
        break
    
    for neighbor in graph[node]:
        if 0 <= neighbor <= 100000 and neighbor not in visited:        
        #if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = node
            queue.append(neighbor)

# 경로 복원 역추적
path = []
current = K
while current is not None:
    path.append(current)
    current = parent[current]
path.reverse()

#print(len(path) - 1)
for x in path:
    print(str(x) + ' ')