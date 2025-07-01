import sys
input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().rstrip().split())
max_score = [a, b, c]
min_score = [a, b, c]

for i in range(1, N):
    a, b, c = map(int, input().rstrip().split())
    prev_a, prev_b, prev_c = max_score
    max_score[0] = max(prev_a, prev_b) + a
    max_score[1] = max(prev_a, prev_b, prev_c) + b
    max_score[2] = max(prev_b, prev_c) + c
    
    prev_a, prev_b, prev_c = min_score
    min_score[0] = min(prev_a, prev_b) + a
    min_score[1] = min(prev_a, prev_b, prev_c) + b
    min_score[2] = min(prev_b, prev_c) + c

print(max(max_score), min(min_score))