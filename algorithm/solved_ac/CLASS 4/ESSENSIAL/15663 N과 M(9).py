import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

ans = set(permutations(nums, M))
ans = list(ans)
ans.sort()

for tup in ans:
    for n in tup:
        print(n, end = ' ')
    print()