import sys
input = sys.stdin.readline
#print = sys.stdout.write

K, N = list(map(int, input().rstrip().split()))

lst = []
for i in range(K):
    n = int(input())
    lst.append(n)

right_l = sum(lst) // N
left_l = 1
ans = 0

while left_l <= right_l:
    mid_l = (left_l + right_l) // 2
    #print(left_l, right_l, mid_l)
    n_list = []
    for i in range(K):
        n_list.append(lst[i] // mid_l)
    cnt = sum(n_list)
    if (cnt == N):
        ans = mid_l
        #print(ans, "break")
        break
    elif cnt < N:
        right_l = mid_l - 1
        #print("go left")
    else:
        left_l = mid_l + 1
        #print("go right")

left_l = 1  # 최소 길이는 1부터 시작
right_l = max(lst)
ans = 0

while left_l <= right_l:
    mid_l = (left_l + right_l) // 2
    cnt = sum(l // mid_l for l in lst)
    
    if cnt >= N:
        ans = mid_l  # 조건 만족: 더 긴 길이 시도
        left_l = mid_l + 1
    else:
        right_l = mid_l - 1

print(ans)