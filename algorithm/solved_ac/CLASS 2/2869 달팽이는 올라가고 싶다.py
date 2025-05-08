import math

A, B, V = list(map(int,input().split()))

days = (V - A) / (A - B)
ans = math.ceil(days) + 1
print(ans)