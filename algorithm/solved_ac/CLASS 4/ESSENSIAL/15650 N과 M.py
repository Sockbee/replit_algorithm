import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) #1부터 N까지 자연수에 M개의 수

nums = range(1, N + 1)
combi = list(combinations(nums, M))

for tup in combi:
    for i in range(M):
        print(tup[i], end = ' ')
    print()