MOD = 1000000007

# 행렬 곱셈 함수
def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, 
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, 
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

# 행렬 거듭제곱 함수
def matrix_pow(M, power):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    base = M
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2
    
    return result

# n번째 피보나치 수 구하기
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    F = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(F, n - 1)
    
    return result_matrix[0][0]  # F(n) 값은 행렬의 (0, 0) 위치에 있음

# 입력 받기
n = int(input())
print(fibonacci(n))