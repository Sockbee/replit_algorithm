import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = []
for i in range(N):
    a, b = list(map(int,input().rstrip().split()))
    arr.append([a, b, i, 0]) #몸무게, 키, 원래 순서, 등수

#arr.sort(key=lambda x: (x[0], x[1])) #몸무게 다음 키 순 정렬
#둘 다 큰사람만 큰거기 때문에 정렬 할 필요가 없었다.


for i in range(N):
    cnt = 0
    for j in range(N):
        if (arr[i][1] < arr[j][1] and arr[i][0] < arr[j][0]):
            cnt += 1
    arr[i][3] = cnt
#print(arr)
#arr.sort(key=lambda x: (x[2]))

for i in range(N):
    print(str(arr[i][3] + 1) + ' ')