# 전위 순회
def preorder(node):
    if node == 0:
        return
    print(ALPHABET[node], end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회
def inorder(node):
    if node == 0:
        return
    inorder(tree[node][0])
    print(ALPHABET[node], end='')
    inorder(tree[node][1])

# 후위 순회
def postorder(node):
    if node == 0:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(ALPHABET[node], end='')


DICTIONARY = {'.':0, 'A':1, 'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
              'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
              'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
              'V':22,'W':23,'X':24,'Y':25,'Z':26,}
ALPHABET = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = int(input())
tree = [[0, 0] for _ in range(N+1)]
for _ in range(N):
    node, left, right = map(DICTIONARY.get, input().split())
    tree[node][0] = left
    tree[node][1] = right

preorder(1)
print()
inorder(1)
print()
postorder(1)