import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) #표의 크기 N, 합 구하는 횟수 M

nums = [[] for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    nums[i] = lst

haps = [[] for _ in range(M)]

for i in range(M):
    lst = list(map(int, input().rstrip().split()))
    haps[i] = lst

dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = nums[0][0]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        if i > 0 and j > 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + nums[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + nums[i][j]
        else:
            dp[i][j] = dp[i - 1][j] + nums[i][j]

for i in range(M):
    x1, y1, x2, y2 = haps[i]
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    
    if x1 == 0 and y1 == 0:
        ans = dp[x2][y2]
    elif x1 > 0 and y1 > 0:
        ans = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    elif x1 == 0:
        ans = dp[x2][y2] - dp[x2][y1 - 1]
    elif y1 == 0:
        ans = dp[x2][y2] - dp[x1 - 1][y2]
    
    print(ans)