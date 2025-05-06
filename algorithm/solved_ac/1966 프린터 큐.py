import sys
input = sys.stdin.readline
#print = sys.stdout.write

T = int(input().rstrip())
for _ in range(T):
    N, M = list(map(int, input().rstrip().split()))
    lst = []
    nums = list(map(int, input().rstrip().split()))
    for i in range(N):
        lst.append([i, nums[i]])

    for i in range(N):
        flag = 0
        for j in range(1, N):
            if (lst[i][1] < lst[j][1]):
                flag = 1
                num = lst.pop(i)
                lst.append(num)
            print(lst)
        print(lst)
                
    for i in range(N):
        if (M == lst[i][0]):
            print(str(i + 1))
