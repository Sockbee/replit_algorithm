import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) #1~N까지의 수 중 M개를 선택
nums = list(map(int, input().rstrip().split()))
nums.sort()

s = []
visited = set()
def dfs(start):
    if len(s)==m:
        chk = ' '.join(map(str,s))
        if chk not in visited:
            visited.add(chk)
            print(chk)
        return
    
    for i in range(start, n):
        s.append(nums[i])
        dfs(i)
        s.pop()
    
dfs(0)