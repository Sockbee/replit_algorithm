import sys
input = sys.stdin.readline
print = sys.stdout.write

K = int(input().rstrip())

stack = []
for _ in range(K):
    n = int(input().rstrip())
    if (n == 0):
        stack.pop()
    else:
        stack.append(n)

ans = sum(stack)
print(str(ans))