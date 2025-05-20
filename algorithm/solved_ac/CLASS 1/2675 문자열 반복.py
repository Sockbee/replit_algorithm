import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for i in range(T):
    n, word = input().rstrip().split()
    n = int(n)
    _len = len(word)
    for j in range(_len):
        print(word[j] * n)
    print('\n')