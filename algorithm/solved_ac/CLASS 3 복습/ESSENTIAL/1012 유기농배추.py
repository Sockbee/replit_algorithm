import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽

for _ in range(T):
    M, N, K = map(int, input().rstrip().split()) # 가로길이 세로길이 배추개수
    graph = [[0 for i in range(M)] for j in range(N)]
    bachus = set()

    for i in range(K):
        a, b = map(int, input().rstrip().split())
        graph[b][a] = 1
        bachus.add((b, a))

    q = deque()
    visited = [[False for i in range(M)] for j in range(N)]

    cnt = 0
    while bachus:
        b, a = bachus.pop()
        q.append((b, a))
        visited[b][a] = True
        while q:
            y, x = q.popleft()

            for i in range(4):  # 네 방향 탐색
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 벗어나면 무시
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue

                # 갈 수 없거나 이미 방문한 곳 무시
                if graph[ny][nx] == 0 or visited[ny][nx]:
                    continue

                q.append((ny, nx))
                bachus.remove((ny, nx))
                visited[ny][nx] = True

        cnt += 1
    
    print(cnt)

#for 루프로 전체 그래프 순회해서 graph == 1이고 not visited일 때 bfs 돌리는게 좀더 효율적