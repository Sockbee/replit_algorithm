import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
nums = [0 for i in range(10001)]
for _ in range(N):
    n = int(input().rstrip())
    nums[n] = nums[n] + 1

for i in range(10001):
    if (nums[i] != 0):
        for _ in range(nums[i]):
            print(str(i) + '\n')