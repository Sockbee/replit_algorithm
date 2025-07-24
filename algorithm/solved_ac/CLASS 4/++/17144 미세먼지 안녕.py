import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())  # R행 C열, T초 후

graph = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치
purifier = 0
for i in range(R):
    if graph[i][0] == -1:
        purifier = i
        break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while time < T:
    time += 1

    # 1. 미세먼지 확산
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                spread_amount = graph[i][j] // 5
                count = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != -1:
                        temp[ni][nj] += spread_amount
                        count += 1
                temp[i][j] -= spread_amount * count

    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1:
                graph[i][j] += temp[i][j]

    # 2. 공기청정기 작동

    # 위쪽: 반시계 방향
    for i in range(purifier - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    for j in range(C - 1):
        graph[0][j] = graph[0][j + 1]
    for i in range(purifier):
        graph[i][C - 1] = graph[i + 1][C - 1]
    for j in range(C - 1, 1, -1):
        graph[purifier][j] = graph[purifier][j - 1]
    graph[purifier][1] = 0

    # 아래쪽: 시계 방향
    for i in range(purifier + 2, R - 1):
        graph[i][0] = graph[i + 1][0]
    for j in range(C - 1):
        graph[R - 1][j] = graph[R - 1][j + 1]
    for i in range(R - 1, purifier + 1, -1):
        graph[i][C - 1] = graph[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        graph[purifier + 1][j] = graph[purifier + 1][j - 1]
    graph[purifier + 1][1] = 0

# 최종 미세먼지 양 계산
result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)
