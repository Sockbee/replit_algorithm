import sys
import heapq
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())

    min_heap = []
    max_heap = []
    nums = dict()
    
    for i in range(N):
        op, num = input().rstrip().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, num * -1)
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        else:  # op == 'D'
            if num == 1:
                while max_heap:
                    _max = heapq.heappop(max_heap) * -1
                    if nums.get(_max, 0) > 0:
                        nums[_max] -= 1
                        break
            else:
                while min_heap:
                    _min = heapq.heappop(min_heap)
                    if nums.get(_min, 0) > 0:
                        break


    filtered_nums = [num for num, count in nums.items() if count > 0]

    if filtered_nums:
        max_value = max(filtered_nums)
        min_value = min(filtered_nums)

        print(max_value, min_value)
    else:
        print("EMPTY")
