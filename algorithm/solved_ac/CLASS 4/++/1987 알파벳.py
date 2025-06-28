import sys
input = sys.stdin.readline

_max = 0

def dfs_bitmask(n, m, graph, x, y, used, count):
    global _max
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    _max = max(_max, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            idx = ord(graph[nx][ny]) - ord('A')
            if not (used & (1 << idx)):
                dfs_bitmask(n, m, graph, nx, ny, used | (1 << idx), count + 1)

def solve():
    N, M = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]

    start_idx = ord(graph[0][0]) - ord('A')
    used = 1 << start_idx

    dfs_bitmask(N, M, graph, 0, 0, used, 1)
    print(_max)

solve()
