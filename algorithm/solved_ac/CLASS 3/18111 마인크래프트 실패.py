import sys
input = sys.stdin.readline
import math

N, M, B = map(int, input().rstrip().split())

nums = []
for i in range(N):
    num = list(map(int, input().rstrip().split()))
    nums.append(num)

_avg = sum(sum(num) for num in nums) / (N * M)

up_avg = 0
low_avg = 0
if _avg >= 256:
    up_avg = 255
    low_avg = 255
else:
    up_avg = math.ceil(_avg)
    if (up_avg != 0):
        low_avg = up_avg - 1

cnt_time = 0
up_time = 0

for i in range(N):
    for j in range(M):
        gap = nums[i][j] - up_avg
        if (gap > 0):
            cnt_time += gap * 2
            B += 1
        elif (gap < 0):
            cnt_time += gap * -1
            B -= 1

if B >= 0:
    up_time = cnt_time

cnt_time = 0
for i in range(N):
    for j in range(M):
        gap = nums[i][j] - low_avg
        if (gap > 0):
            cnt_time += gap * 2
            B += 1
        elif (gap < 0):
            cnt_time += gap * -1
            B -= 1

if up_time:
    if (up_time <= cnt_time):
        print(up_time, up_avg)
    else:
        print(cnt_time, low_avg)
else:
    print(cnt_time, low_avg)