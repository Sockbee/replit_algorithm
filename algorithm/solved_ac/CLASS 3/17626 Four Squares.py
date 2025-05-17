import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i  # 최악의 경우 1을 i번
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1
            
print(dp[n])