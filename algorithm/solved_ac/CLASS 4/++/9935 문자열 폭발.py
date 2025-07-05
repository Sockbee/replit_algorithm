import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
l = len(str2)
stack = []

for ch in str1:
    stack.append(ch)
    if len(stack) >= l and ''.join(stack[-l:]) == str2:
        del stack[-l:]

result = ''.join(stack)
print(result if result else "FRULA")