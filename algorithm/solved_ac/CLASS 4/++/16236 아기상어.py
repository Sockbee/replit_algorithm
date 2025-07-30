import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    graph[i] = lst

dx = [-1, 0, 0, 1]  # 상, 좌, 우, 하
dy = [0, -1, 1, 0]

lv = [2, 0]
fishes = dict()  # 물고기의 크기별로 저장
for i in range(1, 7):
    fishes[i] = 0

start_x = 0
start_y = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and graph[i][j] != 9:
            fishes[graph[i][j]] += 1
        elif graph[i][j] == 9:
            start_x = i
            start_y = j
            graph[i][j] = 0

start = (start_x, start_y, 0)


def bfs(start):
    result = 0
    q = deque()
    q.append(start)

    while q:
        if sum(fishes) == 0:  # 더이상 머글 수 있는 물고기가 없음
            break
        x, y, distance = q.popleft()  # 이전 위치부터 다음 먹방까지 이동거리

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue  # 범위 벗어나면 pass
            if graph[nx][ny] != 0 and graph[nx][ny] < lv[0]:
                lv[1] += graph[nx][ny]  # 경험치로 저장
                fishes[graph[nx][ny]] -= 1  # 물고기 수 -1
                graph[nx][ny] = 0  # 밥 먹음
                if lv[1] >= lv[0]:
                    lv[1] -= lv[0]  # 경험치 차감
                    lv[1] += 1  # 레벨업
                q.append((nx, ny, 0))  # 여기로 아기상어 이동
                result += distance  # 이전먹방부터 이동거리 result에 더함
                break  # for문 탈출
            elif graph[nx][ny] > lv[0]:
                continue  # 다음 위치 탐색
            else:  # 크기가 같거나 0이어서 이동만 가능한경우
                q.append((nx, ny, distance + 1))
    return result


print(bfs(start))
