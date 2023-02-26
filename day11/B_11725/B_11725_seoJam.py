import sys
from collections import deque
sys.stdin = open("sample_input.txt")
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

queue = deque()
queue.append(1)
if 1 in [n1, n2]:
    if n1 == 1:
        tree[n2] = 1
    else:
        tree[n1] = 1
elif tree[n1] or tree[n2]:
    if tree[n1]:
        tree[n2] = n1
    else:
        tree[n1] = n2
else:
    q.append([n1, n2])

while q:
    n1, n2 = q.pop(0)

    if tree[n1]:
        tree[n2] = n1
    elif tree[n2]:
        tree[n1] = n2

for i in range(2, N + 1):
    print(tree[i])