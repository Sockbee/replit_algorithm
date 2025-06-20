import sys
input = sys.stdin.readline

def bf(n, graph):
    dist = [0] * (n + 1)

    for i in range(n):
        for u, v, cost in graph:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if i == n - 1:
                    return True  # 음의 사이클 존재
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []

    # 양방향 도로
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T))

    # 단방향 웜홀
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append((S, E, -T))

    if bf(N, graph):
        print("YES")
    else:
        print("NO")