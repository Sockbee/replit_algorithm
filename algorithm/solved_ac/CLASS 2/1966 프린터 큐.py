import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())
ans = []
for _ in range(T):
    N, M = list(map(int, input().rstrip().split()))
    lst = []
    nums = list(map(int, input().rstrip().split()))
    for i in range(N):
        lst.append([i, nums[i]])

    for k in range(N):
        for i in range(N):
            flag = 0
            for j in range(k + 1, N):
                if (lst[k][1] < lst[j][1]):
                    n = lst.pop(k)
                    lst.append(n)
                    flag = 1
                    break
            if (flag == 0): break

                
    for i in range(N):
        if (M == lst[i][0]):
            ans.append(i + 1)
            break

for i in range(T):
    print(str(ans[i]) + '\n')