import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().rstrip().split()) # 정점의 개수 N, 간선의 개수 E

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())

def dijkstra(start):
    distance = [INF] * (N + 1)
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
    return distance

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

ans = min(path1, path2)
if (ans >= INF):
    print(-1)
else:
    print(ans)