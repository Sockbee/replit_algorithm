import sys

input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    #시작 노드에 대해서 초기화
    dist[start] = 0

    #전체 N번의 라운드 반복
    for i in range(n):
        #모든 간선 확인하기
        for j in range(m):
            now = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            #현재 간선을 거쳐서 다른 노드로 이동하는게 더 짧은 경우
            if dist[now] != INF and dist[next_node] > dist[now]+cost:
                dist[next_node] = dist[now]+cost
                if i == n-1:
                    return True
            return False

n, m = map(int, input().split())
edges = []
dist = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

if bf(1):
    #음수 간선의 순환이 존재하는 경우
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            #도달할 수 없는 경우
            print("-1")
        else:
            #도달할 수 있는 경우
            print(dist[i])