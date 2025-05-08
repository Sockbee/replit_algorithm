import sys
import math
from collections import deque
input = sys.stdin.readline
#print = sys.stdout.write

n = int(input().rstrip())
cnt_exclude = math.floor(n * 0.15 + 0.5) #round는 오사오입을 한다..
#print(cnt_exclude)

lst = []
for i in range(n):
    num = int(input().rstrip())
    lst.append(num)

lst.sort()
dq = deque(lst)
#print(dq)

for i in range(cnt_exclude):
    if dq:
        dq.pop()
    if dq:
        dq.popleft()

#print(dq)

_len = len(dq)
_sum = sum(dq)
if (_len != 0):
    ans = math.floor(_sum / _len + 0.5)
else:
    ans = 0

if (n == 0):
    print('0')
else:
    print(str(ans))