import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp1 = [1] * N
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

dp2 = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if nums[j] < nums[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

max_len = 0
for i in range(N):
    max_len = max(max_len, dp1[i] + dp2[i] - 1)

print(max_len)