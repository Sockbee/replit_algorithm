import sys
input = sys.stdin.readline

#마이너스를 만난순간 다음 마이너스를 만날 때까지 빼기

string = input()

i = 0
prev_buho = 0
nums = []
_sum = 0
flag = 1 # 1이면 + -1이면 -
_len = len(string)
while i < _len:
    if (string[i] == '+'):
        num = int(string[prev_buho : i])
        nums.append(num)
        _sum += num * flag
        prev_buho = i + 1
    elif (string[i] == '-'):
        num = int(string[prev_buho : i])
        nums.append(num)
        _sum += num * flag
        if flag != -1:
            flag = flag * (-1)
        prev_buho = i + 1
    elif (string[i] == '\n'):
        num = int(string[prev_buho : i])
        nums.append(num)
        _sum += num * flag
        prev_buho = i + 1

    i = i + 1

#print(nums)
print(_sum)