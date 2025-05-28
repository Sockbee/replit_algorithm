import sys
input = sys.stdin.readline

T = int(input().rstrip())
prt = []

for _ in range(T):
    m, n, x, y = list(map(int, input().rstrip().split()))
    x_lst = []
    mn = m * n
    for i in range(x, mn + 1, m):
        x_lst.append(i)
    y_lst = []
    for i in range(y, mn + 1, n):
        y_lst.append(i)

    ans = set(x_lst) & set(y_lst)
    if ans:
        print(min(ans))
    else:
        print('-1')
