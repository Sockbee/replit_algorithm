import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

word = input().split('I')
if word[-1] == 'O':
    #print(word[-1])
    word.pop()
if word[0] == 'O':
    word.pop(0)
#print(word)
_len = len(word)
flag = 0 # 이전 원소가 O였는지

ans = 0
cnt = 0
for i in range(_len):
    if flag:
        if word[i] == 'O':
            #print("case1")
            cnt += 1
        else:
            if (cnt >= N):
                ans += (cnt - N + 1)
            #print("case2")
            flag = 0
            #cnt = 0
    else:
        if word[i] == 'O':
            flag = 1
            cnt = 1
            #print("case3")
        else:
            flag = 0
            #print("case4")

print(ans)