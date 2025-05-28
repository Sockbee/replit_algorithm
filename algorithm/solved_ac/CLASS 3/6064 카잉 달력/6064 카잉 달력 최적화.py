import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    found = False
    max_year = m * n  # 최악의 경우

    for k in range(x, max_year + 1, m):
        if (k - y) % n == 0:
            print(k)
            found = True
            break

    if not found:
        print(-1)
