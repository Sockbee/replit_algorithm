import sys
input = sys.stdin.readline

N, M = list(map(int, input().rstrip().split()))

arr_money = []
d = [10001] * 10001
for _ in range(N):
    a = int(input().rstrip())
    arr_money.append(a)

#d[3] = d[5] = 1
for money in arr_money:
    d[money] = 1


#for i in range(6, n + 1):
#    d[i] = min(d[i-3], d[i-5]) + 1
max_money = arr_money[-1]
for i in range(max_money + 1, M + 1):
    d[i] = min(d[i - money] for money in arr_money) + 1

if (d[M] >= 10000):
    print(-1)
else:
    print(d[M])