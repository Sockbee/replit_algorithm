import sys
input = sys.stdin.readline

# 반복 DFS 함수 정의
def dfs_iter(start, graph, V):
    visited = [False] * (V + 1)
    stack = [(start, 0)]
    max_dist = 0
    farthest_node = start

    while stack:
        node, dist = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if dist > max_dist:
            max_dist = dist
            farthest_node = node
        for next_node, weight in graph[node]:
            if not visited[next_node]:
                stack.append((next_node, dist + weight))

    return max_dist, farthest_node

# 입력 처리
V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    lst = input().split()
    u = int(lst[0])
    idx = 1
    while lst[idx] != '-1':
        v = int(lst[idx])
        w = int(lst[idx + 1])
        graph[u].append((v, w))
        idx += 2

# 첫 DFS: 아무 노드에서 가장 먼 노드 찾기
_, farthest_node = dfs_iter(1, graph, V)

# 두 번째 DFS: 해당 노드에서 가장 먼 거리 = 트리의 지름
max_distance, _ = dfs_iter(farthest_node, graph, V)

print(max_distance)
