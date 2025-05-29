import sys
import heapq
input = sys.stdin.readline

heap = []

T = int(input().rstrip())

for i in range(T):
    x = int(input().rstrip())
    if not x:
        if heap:
            min_abs_val, val = heapq.heappop(heap)
            print(val)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))