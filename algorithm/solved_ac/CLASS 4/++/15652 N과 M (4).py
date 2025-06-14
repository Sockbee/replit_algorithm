import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) #1~N까지의 수 중 M개를 선택

s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        #print("dfs", i)
        dfs(i)
        s.pop()
    
dfs(1)