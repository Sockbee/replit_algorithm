import sys
input = sys.stdin.readline

R, C, T = map(int, input().split()) # R행 C열 구하는 T초 시간 후

graph = [[] for _ in range(R)]

for i in range(R):
    lst = list(map(int, input().split()))
    graph[i] = lst

#공기청정기 머리 위치 기록
purifier = 0
for i in range(R):
    if graph[i][0] == -1:
        purifier = i
        break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while time < T:
    #1. 미세먼지가 확산된다.
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                kes = []
                for k in range(4):#4방향 탐색
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 > ni or ni >= R or 0 > nj or nj >= C:
                        continue
                    if graph[ni][nj] != -1:
                        kes.append(k)
                added_value = graph[i][j] // 5
                graph[i][j] -= added_value * len(kes)
                for k in kes:
                    ni = i + dx[k]
                    nj = j + dy[k]
                    graph[ni][nj] += added_value

    #2. 공기청정기가 작동한다.
    #공기청정기는 가장 윗행, 아랫행과 두 칸 이상 떨어져 있다.
                    
            