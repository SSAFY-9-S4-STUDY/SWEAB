N = int(input())

def preorder(e):
    if not e:
        return
    print(e, end='')
    preorder(tree[e][0])
    preorder(tree[e][1])


def inorder(e):
    if not e:
        return
    inorder(tree[e][0])
    print(e, end='')
    inorder(tree[e][1])

    
def postorder(e):
    if not e:
        return
    postorder(tree[e][0])
    postorder(tree[e][1])
    print(e, end='')


tree = dict()
for _ in range(N):
    p, c1, c2 = input().split()
    tree[p] = ['', '']
    if c1 != '.':
        tree[p][0] = c1
    if c2 != '.':
        tree[p][1] = c2


preorder('A')
print()
inorder('A')
print()
postorder('A')