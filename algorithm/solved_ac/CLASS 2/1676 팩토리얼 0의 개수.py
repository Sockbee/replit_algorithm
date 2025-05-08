import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
num = math.factorial(N)

cnt = 0
while True:
    if (num % 10 == 0):
        cnt += 1
        num = num // 10
    else:
        break

print(str(cnt))