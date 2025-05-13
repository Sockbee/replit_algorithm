import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

words = dict()
for i in range(N):
    word = input().rstrip().split()
    words[word[0]] = word[1]

for i in range(M):
    word = input().rstrip()
    print(words[word])