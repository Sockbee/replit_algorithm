import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())

graph = [i for i in range(101)]

for i in range(n+m):
    start, end = map(int, input().rstrip().split())
    graph[start] = end

queue = deque()
visited = [-1 for _ in range(101)]
queue.append(1)
visited[1] = 0

while queue:
    x = queue.popleft()

    for i in range(1, 7):
        nx = x + i

        if nx > 100 or visited[nx] != -1:
            continue
        
        if nx != graph[nx] and visited[graph[nx]] == -1:
            visited[graph[nx]] = visited[x] + 1
        visited[nx] = visited[x] + 1
        queue.append(graph[nx])

print(visited[100])