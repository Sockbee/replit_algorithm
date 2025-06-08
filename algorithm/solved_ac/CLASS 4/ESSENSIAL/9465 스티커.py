import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())

    nums = [[], []]

    for i in range(2):
        lst = list(map(int, input().rstrip().split()))
        nums[i] = lst

    dp = [[0] * N for _ in range(2)]

    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]

    if N > 1:
        dp[0][1] = nums[1][0] + nums[0][1]
        dp[1][1] = nums[0][0] + nums[1][1]

    for i in range(2, N):
        for j in range(2):
            dp[j][i] = max(dp[(j + 1) % 2][i - 2], dp[(j + 1) % 2][i - 1], dp[j][i - 2]) + nums[j][i]
            
    print(max(max(dp[0]), max(dp[1])))