import sys
input = sys.stdin.readline


N = int(input())

stairs = [0] * 301

for i in range(1, N + 1):
    stairs[i] = int(input())

d = [0] * 301

d[1] = stairs[1]
d[2] = stairs[1] + stairs[2]
d[3] = stairs[3] + max(stairs[1], stairs[2])

for i in range(4, N + 1):
    d[i] = max(d[i - 2], stairs[i - 1] + d[i - 3]) + stairs[i]

print(d[N])