# 전위순회로 트리 입력
# 왼쪽 subtree 의 키는 무조건 parent 보다 작다
# 오른쪽 subtree 의 키는 무조건 parent 보다 크다


def post_order(node):
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node)


pre_order = []
for i in range(10000):
    try:
        pre_order.append(int(input()))
    except:
        break

root = pre_order[0]

tree = dict()

for node in pre_order:
    tree[node] = [0, 0]

stack_left = [root]
stack_right = [root]

# print(pre_order)

for node in pre_order:
    if node < root:
        if node < stack_left[-1]:
            tree[stack_left[-1]][0] = node
            stack_left.append(node)
        elif node > stack_left[-1]:
            while stack_left:
                current = stack_left.pop()
                if current > node:
                    tree[prev][1] = node
                    stack_left.append(current)
                    stack_left.append(node)
                    break
                prev = current
            else:
                tree[current][1] = node
                stack_left.append(current)
    elif node > root:
        if node < stack_right[-1]:
            tree[stack_right[-1]][0] = node
            stack_right.append(node)
        elif node > stack_right[-1]:
            while stack_right:
                current = stack_right.pop()
                if current > node:
                    tree[prev][1] = node
                    stack_right.append(current)
                    break
                prev = current
            else:
                tree[current][1] = node
                stack_right.append(node)

print(tree)
post_order(root)

"""
50
30
24
5
27
25
26
28
29
45
98
52
60
106
109
108
110
"""
