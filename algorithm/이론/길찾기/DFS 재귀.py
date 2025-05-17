import sys
sys.setrecursionlimit(10000)  # 재귀 깊이를 늘려서 스택 오버플로우 방지

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


# 그래프의 정점 수와 간선 수를 입력받음
n, m = map(int, input().split())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프라면 양방향으로 간선 추가

# 방문 여부를 기록하는 리스트
visited = [False] * (n + 1)

# DFS 시작
dfs(graph, 1, visited)  # 1번 정점에서 시작
