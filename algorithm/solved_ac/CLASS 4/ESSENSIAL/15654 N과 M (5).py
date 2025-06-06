import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) #1부터 N까지 자연수에 M개의 수

nums = map(int, input().rstrip().split())
combi = list(permutations(nums, M))

combi.sort()

for tup in combi:
    for i in range(M):
        print(tup[i], end = ' ')
    print()