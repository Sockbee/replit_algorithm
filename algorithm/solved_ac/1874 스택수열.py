import sys
from collections import deque
input = sys.stdin.readline
#print = sys.stdout.write

n = int(input().rstrip())

nums = [int(input()) for _ in range(n)]
nums_range = deque(range(1, n + 1))

lst = [0]
ans = []
printing_lst = []

i = 0
j = 0
while i < n and j == 0:
    if (lst[-1] < nums[i]):
        if (nums_range):
            #print("lst append", nums_range[0])
            lst.append(nums_range.popleft())
            printing_lst.append('+')
        else:
             j = 1
             #print("!nums_range")
             break
    elif (lst[-1] > nums[i]):
        #print("ans append", lst[-1])
        ans.append(lst.pop())
        if (ans[i] != nums[i]):
             #print("ans[i] != nums[i]")
             j = 1
             break
        printing_lst.append('-')
    else:
            #print("ans append", lst[-1])
            ans.append(lst.pop())
            printing_lst.append('-')
            i = i + 1

#print("j:", j)
if (j != 1):
    for x in printing_lst:
        print(x)
else:
     print("NO")