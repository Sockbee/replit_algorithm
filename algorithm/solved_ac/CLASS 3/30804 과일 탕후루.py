import sys
from collections import defaultdict as dd
input = sys.stdin.readline

n = int(input().rstrip())
frt = list(map(int, input().rstrip().split()))

left = 0
right = 0
cnt = 0
infos = dd(int)
ans = 0

while right < n:
    #새로운 과일을 추가
    if infos[frt[right]] == 0:
        cnt += 1
    infos[frt[right]] += 1

    while cnt > 2:
        infos[frt[left]] -= 1
        if infos[frt[left]] == 0:
            cnt -= 1
        left += 1

    #최대 길이 갱신
    ans = max(ans, right - left + 1)
    right += 1

print(ans)