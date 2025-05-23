import sys
input = sys.stdin.readline

nums = set()
for i in range(10):
    n = int(input().rstrip())
    nums.add(n % 42)

print(len(nums))