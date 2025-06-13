import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))

dp = [1] * N

for i in range(1, N):
    max_dp = 1
    max_index = -1
    for j in range(i):
        if nums[j] < nums[i] and dp[j] >= max_dp:
            max_dp = dp[j]
            max_index = j
            
    if max_index != -1:
        dp[i] = dp[max_index] + 1

#print(dp)
print(max(dp))