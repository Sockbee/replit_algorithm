import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().split()))
    graph[i] = lst

homes = []
chick = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chick.append((i, j))

min_city_chicken_distance = float('inf')

for combi in combinations(chick, M):
    total_distance = 0
    for home in homes:
        distance = min(abs(home[0] - i) + abs(home[1] - j) for i, j in combi)
        total_distance += distance
    min_city_chicken_distance = min(min_city_chicken_distance, total_distance)

print(min_city_chicken_distance)