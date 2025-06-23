import sys
input = sys.stdin.readline

def pre_order(node):
    if node == '.':
        return
    print(node, end='')
    pre_order(tree[node][0])
    pre_order(tree[node][1])
    
def in_order(node):
    if node == '.':
        return
    in_order(tree[node][0])
    print(node, end='')
    in_order(tree[node][1])
    
def post_order(node):
    if node == '.':
        return
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end='')
    

N = int(input())
tree = dict()
for i in range(N):
    lst = input().rstrip().split()
    tree[lst[0]] = [lst[1], lst[2]]

pre_order('A')
print()
in_order('A')
print()
post_order('A')