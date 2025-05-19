import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = []
for _ in range(N):
    ground.extend(map(int, input().split()))
    #extend 함수는 리스트에 다른 리스트의 요소를 풀어서 덧붙이는 함수
    #[1, 2, 3, [4, 5]] 대신 [1, 2, 3, 4, 5]로

min_time = float('inf')
result_height = 0

for target in range(257):  # 높이 후보: 0~256
    time = 0
    inventory = B
    
    for h in ground:
        if h > target:
            time += (h - target) * 2
            inventory += (h - target)
        else:
            time += (target - h)
            inventory -= (target - h)
    
    if inventory >= 0:
        if time < min_time:
            min_time = time
            result_height = target
        elif time == min_time and target > result_height:
            result_height = target

print(min_time, result_height)
