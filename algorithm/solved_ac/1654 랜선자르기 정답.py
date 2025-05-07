import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

left = 1  # 최소 길이는 1
right = max(lst)
ans = 0

while left <= right:
    mid = (left + right) // 2

    if mid == 0:  # 혹시라도 방어
        break

    cnt = sum(l // mid for l in lst)
    
    if cnt >= N:
        ans = mid  # 조건 만족: 더 긴 길이 시도
        left = mid + 1
    else:
        right = mid - 1

print(ans)
