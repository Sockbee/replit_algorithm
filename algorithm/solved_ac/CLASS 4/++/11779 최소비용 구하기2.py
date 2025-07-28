import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수 N , 간선의 개수 M
N = int(input())
M = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(N + 1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N + 1)
prev = [0] * (N + 1)  # 이전 노드를 저장할 리스트 추가

#모든 간선 정보 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
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
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                prev[next_node] = now  # 이전 노드 기록
                heapq.heappush(q, (cost, next_node))

dijkstra(start)

path = []
node = end
while node:
    path.append(node)
    node = prev[node]
path.reverse()

print(distance[end])        # 최단 거리
print(len(path))            # 경로에 포함된 노드 수
print(*path)                # 경로 출력