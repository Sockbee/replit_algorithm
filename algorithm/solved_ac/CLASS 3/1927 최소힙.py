import sys
import heapq
input = sys.stdin.readline

heap = []

n = int(input().rstrip())

for i in range(n):
  x = int(input().rstrip())
  if not x:
    if heap:
      min_val = heapq.heappop(heap)
      print(min_val)
    else:
      print(0)
  else:
    heapq.heappush(heap, x)
