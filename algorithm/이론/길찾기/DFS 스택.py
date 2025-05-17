def dfs_stack(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            
            # 인접 노드를 스택에 추가 (내림차순으로 삽입하면, 오름차순 탐색)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)


# 그래프와 시작 노드 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프라면 양방향으로 간선 추가

# DFS 시작
dfs_stack(graph, 1)  # 1번 정점에서 시작
