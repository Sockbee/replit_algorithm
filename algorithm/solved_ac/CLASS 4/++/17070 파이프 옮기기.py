import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

d = [[[0]*3 for _ in range(N)] for _ in range(N)]
d[0][1][0] = 1  # 초기 상태: (0,1) 위치에 가로 방향

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: continue
        # 가로
        if j >= 1 and graph[i][j-1] == 0:
            d[i][j][0] += d[i][j-1][0] + d[i][j-1][2]
        # 세로
        if i >= 1 and graph[i-1][j] == 0:
            d[i][j][1] += d[i-1][j][1] + d[i-1][j][2]
        # 대각선
        if i >= 1 and j >= 1 and graph[i-1][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j-1] == 0:
            d[i][j][2] += d[i-1][j-1][0] + d[i-1][j-1][1] + d[i-1][j-1][2]

print(sum(d[N-1][N-1]))