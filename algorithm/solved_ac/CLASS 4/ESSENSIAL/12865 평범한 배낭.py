import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

items = [[] for i in range(N)]

for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    items[i] = lst

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = items[i - 1]
    for k in range(K + 1):
        if w > k:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w] + v)

print(dp[N][K])