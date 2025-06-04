import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) #N이 세로, M이 가로

graph = [[] for _ in range(N)]
ans = [[0 for _ in range(M)] for _ in range(N)]  # 수정된 초기화

for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    graph[i] = lst

for i in range(N):
    for j in range(M):
        #정사각형
        if i + 1 < N and j + 1 < M:
            ans[i][j] = graph[i][j] + graph[i][j + 1] + graph[i + 1][j] + graph[i + 1][j + 1]
        #길쭉한 애 세로
        if i + 3 < N:
            ans[i][j] = max(ans[i][j], graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j])
        #길쭉한 애 가로
        if j + 3 < M:
            ans[i][j] = max(ans[i][j], graph[i][j + 1] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3])
        # 3 가로
        if 0 < j < M - 1:
            if 0 < i < N - 1:
                ans[i][j] = max(ans[i][j], graph[i][j-1] + graph[i][j] + graph[i][j+1] 
                                + max(graph[i-1][j-1], graph[i-1][j], graph[i-1][j+1],
                                      graph[i+1][j-1], graph[i+1][j]), graph[i+1][j+1])
            elif i == 0:
                ans[i][j] = max(ans[i][j], graph[i][j-1] + graph[i][j] + graph[i][j+1] 
                                + max(graph[i+1][j-1], graph[i+1][j]), graph[i+1][j+1])
            elif i == N - 1:
                ans[i][j] = max(ans[i][j], graph[i][j-1] + graph[i][j] + graph[i][j+1] 
                                + max(graph[i-1][j-1], graph[i-1][j], graph[i-1][j+1]))

        # 3 세로
        if 0 < i < N - 1:
            if 0 < j < M - 1:
                ans[i][j] = max(ans[i][j], graph[i-1][j] + graph[i][j] + graph[i+1][j] 
                                + max(graph[i-1][j-1], graph[i][j-1], graph[i+1][j-1],
                                      graph[i-1][j+1], graph[i][j+1], graph[i+1][j+1]))
            elif j == 0:
                ans[i][j] = max(ans[i][j], graph[i-1][j] + graph[i][j] + graph[i+1][j] 
                                + max(graph[i-1][j+1], graph[i][j+1], graph[i+1][j+1]))
            elif j == M - 1:
                ans[i][j] = max(ans[i][j], graph[i-1][j] + graph[i][j] + graph[i+1][j] 
                                + max(graph[i-1][j-1], graph[i][j-1], graph[i+1][j-1]))

        #번개 가로
        if 0 < j < M - 1 and i < N - 1:
            ans[i][j] = max(ans[i][j], graph[i][j] + graph[i+1][j] 
                            + max(graph[i][j-1] + graph[i+1][j+1], graph[i+1][j-1] + graph[i][j+1]))
        #번개 세로
        if 0 < i < N - 1 and j < M - 1:
            ans[i][j] = max(ans[i][j], graph[i][j] + graph[i][j+1] 
                            + max(graph[i-1][j] + graph[i+1][j+1], graph[i-1][j+1] + graph[i+1][j]))
            
max_val = max(map(max, ans))
print(max_val)