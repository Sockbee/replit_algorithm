import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

#노드 수, 간선 수, 목적지
N, M, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]
graph_reversed = [[] for _ in range(N + 1)]
distance_forward = [INF] * (N + 1)
distance_reversed = [INF] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph_reversed[b].append((a, c))
    

def dijkstra(start, graph, distance):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X, graph, distance_forward)
dijkstra(X, graph_reversed, distance_reversed)

result = [x + y for x, y in zip(distance_forward, distance_reversed)]
print(max(result[1:N+1]))