import sys
input = sys.stdin.readline

N = int(input().rstrip())

graph = [[] for _ in range(N + 1)]
nums = [False] * (N + 1)
nums[1] = True

for i in range(N - 1):
    a, b = map(int, input().rstrip().split())
    if nums[a]:
        graph[a].append(b)
        nums[b] = True
    elif nums[b]:
        graph[b].append(a)
        nums[a] = True

ans = [0] * (N + 1)
for i in range(1, N + 1):
    for num in graph[i]:
        ans[num] = i

for i in range(2, N + 1):
    print(ans[i])