def make4(n):
    while len(n) < 4:
        n = "0" + n
    return n

n = "10"

print(make4(n))