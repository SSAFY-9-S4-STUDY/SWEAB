import sys
sys.stdin = open("input.txt")


class Node:
    def __init__(self, data, ln, rn):
        self.data = data
        self.ln = ln
        self.rn = rn


def pre_order(node):
    print(node.data, end= '')
    if node.ln != None:
        pre_order(tree[node.ln])
    if node.rn != None:
        pre_order(tree[node.rn])
    

def in_order(node):
    if node.ln != None:
        in_order(tree[node.ln])
    print(node.data, end= '')
    if node.rn != None:
        in_order(tree[node.rn])


def post_order(node):
    if node.ln != None:
        post_order(tree[node.ln])
    if node.rn != None:
        post_order(tree[node.rn])
    print(node.data, end= '')
    
N = int(input())
tree = {}
for i in range(N):
    data, ln, rn = input().split()
    if ln == '.':
        ln = None
    if rn == '.':
        rn = None
    tree[data] = Node(data, ln, rn)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()




