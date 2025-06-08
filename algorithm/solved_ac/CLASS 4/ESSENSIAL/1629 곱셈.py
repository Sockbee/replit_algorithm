import sys
input = sys.stdin.readline

#나머지 정리 (a * b) % c == ((a % c) * (b % c)) % c
def mod_power(a, n, c):
    result = 1
    a = a % c  # 미리 모듈로 연산
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        n //= 2
    return result

# A를 B번 곱한 수를 C로 나눈 나머지를 출력
A, B, C = map(int, input().rstrip().split())
print(mod_power(A, B, C))