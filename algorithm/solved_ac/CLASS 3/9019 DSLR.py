import sys
from collections import deque
input = sys.stdin.readline

def op_D(n):
    return (2 * n) % 10000

def op_S(n):
    return 9999 if n == 0 else n - 1
    
def op_L(n):
    n = str(n).zfill(4)
    return int(n[1:] + n[0])

def op_R(n):
    n = str(n).zfill(4)
    return int(n[-1] + n[:-1])

op = ['D', 'S', 'L', 'R']


T = int(input())

for _ in range(T):
    a, b = map(int, input().rstrip().split())

    q = deque()
    visited = [False] * 10000
    prev = [(-1, '') for _ in range(10000)]

    visited[a] = True
    q.append(a)

    while q:
        x = q.popleft()
        if x == b:
            break

        for i, func in enumerate([op_D, op_S, op_L, op_R]):
            nx = func(x)
            if not visited[nx]:
                visited[nx] = True
                prev[nx] = (x, op[i])
                q.append(nx)

    # 백트래킹
    path = []
    current = b
    while current != a:
        current, oper = prev[current]
        path.append(oper)

    print(''.join(reversed(path)))
