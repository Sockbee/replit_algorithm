import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 재귀 깊이를 늘려서 스택 오버플로우 방지
from collections import deque

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end = ' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 그래프의 정점 수와 간선 수를 입력받음
N, M, V = map(int, input().rstrip().split())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프라면 양방향으로 간선 추가

# 각 노드의 간선 리스트를 오름차순으로 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 방문 여부를 기록하는 리스트
visited_dfs = [False] * (N + 1)

# DFS 시작
dfs(graph, V, visited_dfs)  # V 정점에서 시작
print()
bfs(graph, V)