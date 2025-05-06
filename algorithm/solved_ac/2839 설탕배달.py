import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

namerge = N % 5
cnt_5 = 0
cnt_3 = 0
ans = 0
if (namerge == 0):
    cnt_5 = N // 5
elif (namerge == 1):
    if (N - 6 >= 0):
        N = N - 6
        cnt_5 = N // 5
        cnt_3 = 2
    else:
        ans = -1
elif (namerge == 2):
    if (N - 12 >= 0):
        N = N - 12
        cnt_5 = N // 5
        cnt_3 = 4
    else:
        ans = -1
elif (namerge == 3):
    N = N - 3
    cnt_5 = N // 5
    cnt_3 = 1

elif (namerge == 4):
    if (N - 9 >= 0):
        N = N - 9
        cnt_5 = N // 5
        cnt_3 = 3
    else:
        ans = -1
else:
    cnt_5 = N // 5

if (ans != -1):
    print(str(cnt_3 + cnt_5))
else:
    print(str(ans))