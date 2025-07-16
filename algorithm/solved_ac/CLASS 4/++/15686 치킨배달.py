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
        if i == 1:
            homes.append((i, j))
        elif i == 2:
            chick.append((i, j))

for combi in list(combinations(chick, M)):
    for home in homes:
