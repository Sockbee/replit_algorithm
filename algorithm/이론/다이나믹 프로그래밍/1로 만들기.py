import sys
input = sys.stdin.readline

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    #현재의 수에서 1을 빼는 경우와 
    #나머지 5, 3, 2로 나누어 떨어지는 것 중에 작은것을 선택
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])