import sys
input = sys.stdin.readline

X = 1000000007

M = int(input())
_sum = 0
for i in range(M):
    N, S = map(int, input().split())
    # N/S를 모듈러로 표현
    N_inv = pow(N, X - 2, X)
    result = (S * N_inv) % X
    _sum += result

print(_sum % X)