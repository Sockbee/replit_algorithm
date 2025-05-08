import sys
input = sys.stdin.readline
#print = sys.stdout.write

K, N = list(map(int, input().rstrip().split()))

nums = [int(input()) for _ in range(K)]

left = 1
right = max(nums)
ans = 0
#cnt = 0

#이분탐색 left right +- 1 설명 -> 어차피 mid가 답이 아닌걸 알았으니까
#mid - 1을 닫힌구간으로 보면 이 안에 있다!
#이분탐색은 정수에서만 탐색 가능!
while left <= right:
    mid = (left + right) // 2
    #cnt = 0
    #for num in nums:
    #    cnt += num // mid
    #sum generator 사용이 실행시간에 큰 영향
    cnt = sum(num // mid for num in nums)

    if (cnt < N):
        right = mid - 1
    else:
        left = mid + 1
        ans = mid

print(ans)