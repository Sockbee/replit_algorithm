import sys
input = sys.stdin.readline

A, B = map(int, input().split())
matrix = [[] for _ in range(A)]
for i in range(A):
    lst = list(map(int, input().split()))
    matrix[i] = lst

def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000  # 각 원소에 대해 1000으로 나눈 나머지
    return C

def mat_pow(A, power):
    n = len(A)
    # 단위행렬(Identity matrix) 준비
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while power > 0:
        if power % 2 == 1:
            result = matmul(result, A)
        A = matmul(A, A)
        power //= 2
    return result

A_cubed = mat_pow(matrix, B)

for row in A_cubed:
    print(' '.join(map(str, row)))
