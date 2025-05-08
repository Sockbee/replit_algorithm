import sys
input = sys.stdin.readline
print = sys.stdout.write

lines = []

while True:
    line = input().rstrip()
    if line == ".":
        break
    lines.append(line)

left = ['(', '[']
ans = []

for line in lines:
    stack = []
    ans_temp = ""

    for alphabet in line:
        if (alphabet in left):
            stack.append(alphabet)
        elif (alphabet == ')'):
            if (stack and stack[-1] == '('):
                stack.pop()
            else:
                ans_temp = "no"
                break
        elif (alphabet == ']'):
            if (stack and stack[-1] == '['):
                stack.pop()
            else:
                ans_temp = "no"
                break
    if (ans_temp != "no"):
        ans_temp = "yes" if not stack else "no"
    ans.append(ans_temp)

for word in ans:
    print(word + '\n')