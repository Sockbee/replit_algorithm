import sys
input = sys.stdin.readline
from functools import reduce

T = int(input().rstrip())
#ans = []
#dct = []
for i in range(T):
    n = int(input().rstrip())
    wears = [0] * 30
    wear_type = dict()
    cnt = 0
    product = 0
    for j in range(n):
        #word[0]이 옷 이름, word[1]이 옷 종류
        word = input().rstrip().split()
        if word[1] not in wear_type:
            wear_type[word[1]] = cnt
            wears[cnt] += 1
            cnt = cnt + 1
        else:
            wears[wear_type[word[1]]] += 1
        
        if cnt > 0:
            product = reduce(lambda x, y: x * y, (x + 1 for x in wears[:cnt])) - 1
        else:
            product = 0  # 0이 아닌 원소가 하나도 없을 경우

    print(product)   
        
#print(ans)            
        