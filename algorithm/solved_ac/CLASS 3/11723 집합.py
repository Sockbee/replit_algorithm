import sys
input = sys.stdin.readline
#print = sys.stdout.write

S = set()

M = int(input())
#ans = ""

for i in range(M):
    words = input().rstrip().split()
    if len(words) == 1:
         if (words[0] == "all"):
            S = set(range(1, 21))
         #elif (words[0] == "empty"):
         else:
            S = set()
    else:
        word, num = words[0], words[1]
        num = int(num)
        if (word == "add"):
            S.add(num)
        elif (word == "remove"):
            S.discard(num)
        elif (word == "check"):
            #if (num in S):
            #    ans += "1"
            #else:
            #    ans += "0"###
            
            print(1 if num in S else 0)
        elif (word == "toggle"):
            if (num in S):
                S.discard(num)
            else:
                S.add(num)
