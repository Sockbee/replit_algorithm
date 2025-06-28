import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())

base = [[' ', ' ', '*', ' ', ' ',], [' ', '*', ' ', '*', ' '], ['*', '*', '*', '*', '*']]

tri = [[' ' for i in range(2 * N - 1)] for j in range(N)]

def recursive_tri(x, y, h):
    if h == 3:
        for i in range(x, x + 3):
            for j in range(y - 2, y + 3):
                tri[i][j] = base[i - x][j - y + 2]
        return
    
    nh = h // 2
    recursive_tri(x, y, nh)
    recursive_tri(x + nh, y - nh, nh)
    recursive_tri(x + nh, y + nh, nh)

recursive_tri(0, N - 1, N)

for row in tri:
    print(''.join(row))