def VLR(v):
    if v != '.':
        print(v, end='')
        VLR(tree_dict[v][0])
        VLR(tree_dict[v][1])


def LVR(v):
    if v != '.':
        LVR(tree_dict[v][0])
        print(v, end='')
        LVR(tree_dict[v][1])


def LRV(v):
    if v != '.':
        LRV(tree_dict[v][0])
        LRV(tree_dict[v][1])
        print(v, end='')


N = int(input())
tree_dict = dict()

for _ in range(N):
    V, L, R = input().split()
    tree_dict[V] = [L, R]

VLR('A')
print()
LVR('A')
print()
LRV('A')
print()