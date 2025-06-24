import sys

input = sys.stdin.readline

precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
output = []
operators = []

expr = input()

for token in expr:
    if token.isdigit() or token.isalpha():
        output.append(token)
    elif token == "(":
        operators.append(token)
    elif token == ")":
        while output and output[-1] != "(":
            output.append(operators.pop())
        output.pop()
    elif token in precedence:
        while (
            operators
            and operators[-1] != "("
            and precedence[operators[-1]] >= precedence[token]
        ):
            output.append(operators.pop())
        operators.append(token)

while operators:
    output.append(operators.pop())

print(''.join(output))