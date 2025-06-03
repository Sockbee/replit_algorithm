import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) #N이 세로, M이 가로

graph = [[] for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    graph[i].append(lst)

visited = set()

for i in range(N):
    for j in range(M):
        cnt = 0
        #DFS로 구현해서 4칸을 visited에
        # ((i, j), (i, j), (i,j) (i, j)) 튜플로 추가해서 in 확인
