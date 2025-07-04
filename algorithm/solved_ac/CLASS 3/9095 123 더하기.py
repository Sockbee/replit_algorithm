import sys
input = sys.stdin.readline

T = int(input().rstrip())
nums = []
for i in range(T):
    n = int(input().rstrip())
    nums.append(n)

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

for num in nums:
    print(d[num])