import sys
input = sys.stdin.readline

N = int(input())

rgb = [[] for _ in range(N + 1)]

ans = []

for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    rgb[i] = lst

dist = [[0]*3 for _ in range(N)]

dist[0][0] = rgb[0][0]
dist[0][1] = rgb[0][1]
dist[0][2] = rgb[0][2]

# 모든 경우의 수를 들고 간다.
for i in range(1, N):
    dist[i][0] = min(dist[i-1][1], dist[i-1][2]) + rgb[i][0]
    dist[i][1] = min(dist[i-1][0], dist[i-1][2]) + rgb[i][1]
    dist[i][2] = min(dist[i-1][0], dist[i-1][1]) + rgb[i][2]

print(min(dist[N-1]))