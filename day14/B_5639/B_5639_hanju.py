import sys
sys.setrecursionlimit(10**6)

# 후위 순회하는 재귀 함수
def postorder_traverse(root):
    if root == 0:
        pass
    else:
        postorder_traverse(trees[root][0])
        postorder_traverse(trees[root][1])
        print(root)

# 전위 순회한 트리 입력받기
numbers = []
while True:
    try:
        numbers.append(int(sys.stdin.readline()))
    except:
        break

# 각 부모 노드의 자식 노드 찾기
trees = {i:[0, 0] for i in numbers}
stack, root = [numbers[0]], numbers[0]

for i in numbers[1:]:
    if i < stack[-1]:
        trees[stack[-1]][0] = i
        stack.append(i)
    else:
        while stack:
            tmp = stack.pop()
            if not stack or i < stack[-1]:
                stack.append(i)
                trees[tmp][1] = i
                break

postorder_traverse(numbers[0])

