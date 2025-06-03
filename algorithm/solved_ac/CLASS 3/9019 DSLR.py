import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def op_D(n):
    n = int(n)
    return str((2 * n) % 10000)

def op_S(n):
    n = int(n)
    if n == 1:
        return "9999"
    else:
        return str(n - 1)
    
def op_L(n):
    rotated_L = n[3] + n[:3]
    return rotated_L

def op_R(n):
    rotated_R = n[1:4] + n[0]
    return rotated_R

for _ in range(T):
    a, b = input().rstrip().split()
    a.zfill(4) # 0 채워서 4자리수로 만듦
    b.zfill(4)

    q = deque()
    visited = [False] * 10000
    visited[a] = True
    q.append(a)

    while q:
        x = q.popleft()
        if x == b:
            break
        
        for nx in [op_D(x), op_S(x), op_L(x), op_R(x)]:
            if not visited[int(nx)]:
                visited[int(nx)] = True
                q.append(nx)

