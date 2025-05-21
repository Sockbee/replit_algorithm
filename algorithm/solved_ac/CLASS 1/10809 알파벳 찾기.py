import sys
input = sys.stdin.readline

word = input().rstrip()

alphabets = [-1] * 26

_len = len(word)

for i in range(_len):
    n = ord(word[i]) - 97
    if (alphabets[n] == -1):
        alphabets[n] = i

for i in range(26):
    print(alphabets[i], end = ' ')