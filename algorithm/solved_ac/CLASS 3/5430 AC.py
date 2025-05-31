import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    func = input().rstrip()
    n = int(input().rstrip())
    nums = input().rstrip()
    err_flag = False

    nums = nums[1:-1]  # 괄호 제거
    dq = deque(nums.split(',')) if nums else deque()

    reversed_flag = False
    for char in func:
        if char == 'R':
            reversed_flag = not reversed_flag
        else:
            if dq:
                if reversed_flag:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                err_flag = True
                break

    if err_flag:
        print("error")
    else:
        if reversed_flag:
            dq.reverse()
        print('[' + ','.join(dq) + ']')