import sys
import math
input = sys.stdin.readline

def lcm(a, b):
    return a * b // math.gcd(a, b)

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    found = False
    max_year = lcm(m, n)  # m과 n의 최소공배수까지만 보면 됨

    for k in range(x, max_year + 1, m):
        if (k - y) % n == 0:
            print(k)
            found = True
            break

    if not found:
        print(-1)
