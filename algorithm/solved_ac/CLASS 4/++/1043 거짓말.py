import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

N, M = map(int, input().split()) # N은 사람의 수, M은 파티의 수
know_p = list(map(int, input().split()))
know_p.pop(0)
parent = [i for i in range(N + 1)]

parties = []

for i in range(M):
    lst = list(map(int, input().split()))
    lst.pop(0)
    parties.append(lst)

for party in parties:
    if len(party) <= 1:
        continue
    first = party[0]
    for person in party[1:]:
        union(first, person)            

truth_roots = set(find(person) for person in know_p)

answer = 0
for party in parties:
    # 파티의 참석자 중 한 명이라도 truth_root와 연결되어 있으면 거짓말 불가
    if any(find(person) in truth_roots for person in party):
        continue
    answer += 1

print(answer)