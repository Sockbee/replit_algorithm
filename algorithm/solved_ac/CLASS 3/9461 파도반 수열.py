import sys
input = sys.stdin.readline

T = int(input())
nums = []
for i in range(T):
    nums.append(int(input()))

max_num = max(nums)

d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

for i in range(6, max_num + 1):
    d[i] = d[i - 1] + d[i - 5]

for num in nums:
    print(d[num])