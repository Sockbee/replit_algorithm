import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

INF = int(1e9)

def zero_one_bfs(start):
    dist = [INF] * 100001
    dist[start] = 0
    dq = deque()
    dq.append(start)

    while dq:
        x = dq.popleft()

        if (x == K):
            break
        
        dx = [2*x, x+1, x-1]
        dt = [0, 1, 1]
        for i in range(3):
            nx = dx[i]
            if (0 <= nx <= 100000) and (dist[nx] > dist[x] + dt[i]):
                dist[nx] = dist[x] + dt[i]
                if dt[i] == 0:
                    dq.appendleft(nx)
                else:
                    dq.append(nx)

    return dist

lst = zero_one_bfs(N)
print(lst[K])