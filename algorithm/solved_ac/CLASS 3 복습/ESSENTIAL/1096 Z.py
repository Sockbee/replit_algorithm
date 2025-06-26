import sys
N, r, c = map(int, sys.stdin.readline().rstrip().split()) #r이 세로 c가 가로

def find_num(start_y, start_x, n, num):
    #print(num)
    if n == 0:
        return num
    
    _len = 2 ** (n - 1)
    if r < _len + start_y and c < _len + start_x:
        #print(0)
        return find_num(start_y, start_x, n - 1, num)
    elif r < _len + start_y and c >= _len + start_x:
        #print(1)
        return find_num(start_y, start_x + _len, n - 1, num + _len ** 2)
    elif r >= _len + start_y and c < _len + start_x:
        #print(2)
        return find_num(start_y + _len, start_x, n - 1, num + 2 * (_len ** 2))
    elif r >= _len + start_y and c >= _len + start_x:
        #print(3)
        return find_num(start_y + _len, start_x + _len, n - 1, num + 3 * (_len ** 2))

ans = find_num(0, 0, N, 0)
print(ans)