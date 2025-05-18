import sys
import heapq
input = sys.stdin.readline

heap = []

n = int(input().rstrip())

for i in range(n):
    x = int(input().rstrip())
    x *= -1
    if not x:
        if heap:
            min_val = heapq.heappop(heap)
            min_val *= -1
            print(min_val)
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
