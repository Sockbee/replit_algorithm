import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())

MAX = 100001
visited = [-1] * MAX       # 방문 시간 저장
prev = [-1] * MAX          # 이전 노드 저장 (경로 역추적용)

queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    x = queue.popleft()

    if x == m:
        break

    next_x = [x - 1, x + 1, 2 * x]

    for i in range(3):
        nx = next_x[i]
        if 0 <= nx < MAX and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            prev[nx] = x
            queue.append(nx)

#경로 역추적 backtracking
path = []
current = m
while current != -1:
    path.append(current)
    current = prev[current]

path.reverse()

print(visited[m])
for num in path:
    print(num, end = ' ')