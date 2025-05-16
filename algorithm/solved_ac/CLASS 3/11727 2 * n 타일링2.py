import sys
input = sys.stdin.readline

d = [0] * 1001

n = int(input().rstrip())

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + 2 * d[i - 2]

print(d[n] % 10007)