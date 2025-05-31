import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input().rstrip())
graph = [[INF] * n for _ in range(n)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
#for a in range(1, n + 1):
#    graph[a][a] = 1

for i in range(n):
    #A에서 B로 가는 비용은 C라고 설정
    nums = list(map(int, input().rstrip().split()))
    for j in range(n):
        if nums[j]:
            graph[i][j] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
#수행된 결과를 출력
for a in range(n):
    for b in range(n):
        #도달할 수 없는 경우 무한이라고 출력
        if graph[a][b] == INF:
            #print("INFINITY", end = " ")
            print(0, end = " ")
        else:
            #print(graph[a][b], end = ' ')
            print(1, end = " ")
    print()