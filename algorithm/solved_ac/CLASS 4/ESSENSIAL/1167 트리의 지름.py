import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node, weight):
    global max_dist, farthest
    visited[node] = True
    if weight > max_dist:
        max_dist = weight
        farthest = node
    for next_node, w in graph[node]:
        if not visited[next_node]:
            dfs(next_node, weight + w)

V = int(input())
graph = [[] for _ in range(V + 1)]

for i in range(V):
    lst = list(map(int, input().rstrip().split()))
    _len = len(lst) - 1
    for j in range(1, _len, 2):
        graph[lst[0]].append((lst[j], lst[j + 1]))

# 1차 DFS - 가장 먼 노드 A를 찾음
visited = [False] * (V + 1)
max_dist = 0
farthest = 0
dfs(1, 0)

# 2차 DFS - A에서 가장 먼 노드까지 거리 = 지름
visited = [False] * (V + 1)
max_dist = 0
dfs(farthest, 0)

print(max_dist)