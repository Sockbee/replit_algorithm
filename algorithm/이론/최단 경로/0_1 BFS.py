from collections import deque

def zero_one_bfs(start, graph, n):
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque()
    dq.append(start)

    while dq:
        cur = dq.popleft()
        for neighbor, weight in graph[cur]:
            if dist[neighbor] > dist[cur] + weight:
                dist[neighbor] = dist[cur] + weight
                if weight == 0:
                    dq.appendleft(neighbor)  # 0은 우선적으로 처리
                else:
                    dq.append(neighbor)      # 1은 나중에 처리
    return dist
