import sys
input = sys.stdin.readline
print = sys.stdout.write

lines = []

while True:
    line = input().rstrip()
    lines.append(line)
    if line == ".":
        break

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
    if (not stack):
        ans_temp = "yes"
    else:
        ans_temp = "no"
    ans.append(ans_temp)

for word in ans:
    print(word + '\n')