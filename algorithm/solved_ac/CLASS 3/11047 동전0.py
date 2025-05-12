import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coins = []
for i in range(N):
    n = int(input().rstrip())
    coins.append(n)

i = N - 1
cnt = 0
while K > 0:
    if (coins[i] > K):
        i = i - 1
        continue
    else:
        cnt += (K // coins[i])
        K = K % coins[i]

print(cnt)