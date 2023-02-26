import sys

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    nod1, nod2 = map(int, sys.stdin.readline().split())
    tree[nod1].append(nod2)
    tree[nod2].append(nod1)

parents, stack = [0]*(N+1), [1]
while stack:
    p = stack.pop()
    for i in tree[p]:
        if tree[i]:
            stack.append(i)
            parents[i] = str(p)
    tree[p] = []

print('\n'.join(parents[2:]))
