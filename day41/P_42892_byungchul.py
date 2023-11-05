import sys
sys.setrecursionlimit(10**4)  # 재귀 깊이 설정(문제 제한 사항)


class Node:
    def __init__(self, node_id, x_coord):
        self.id = node_id  # 노드 고유 id
        self.x = x_coord  # x 좌표
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드


def build_tree(nodes, nodeinfo):  # 정렬된 노드 목록을 받아 이진트리를 구성. 부모노드를 탐색하며 올바른 자식 노드 위치를 찾아 삽입.
    root = Node(*nodes[0])
    node_dict = {root.id: root}
    for node_id, x_coord in nodes[1:]:
        current_node = Node(node_id, x_coord)
        node_dict[node_id] = current_node
        parent = root
        while True:
            if x_coord < parent.x:
                if not parent.left:
                    parent.left = current_node
                    break
                parent = node_dict[parent.left.id]
            else:
                if not parent.right:
                    parent.right = current_node
                    break
                parent = node_dict[parent.right.id]
    return root


def traverse_preorder(node, nodeinfo, route):  # 전위 순회
    if node:
        route.append(node.id)
        traverse_preorder(node.left if node.left else None, nodeinfo, route)
        traverse_preorder(node.right if node.right else None, nodeinfo, route)


def traverse_postorder(node, nodeinfo, route):  # 후위 순회
    if node:
        traverse_postorder(node.left if node.left else None, nodeinfo, route)
        traverse_postorder(node.right if node.right else None, nodeinfo, route)
        route.append(node.id)


def solution(nodeinfo):  # 노드 정보를 인덱스화, y좌표가 큰 순서대로, x좌표가 작은 순서대로 정렬하여 트리 구성.
    indexed_nodeinfo = [(i + 1, x) for i, (x, y) in enumerate(nodeinfo)]
    # Sort nodes first by y desc, then by x asc
    sorted_nodes = sorted(indexed_nodeinfo, key=lambda x: (-nodeinfo[x[0] - 1][1], x[1]))
    # Build the tree
    root = build_tree(sorted_nodes, nodeinfo)
    # Traverse the tree in preorder and postorder
    preorder_route = []
    postorder_route = []
    traverse_preorder(root, nodeinfo, preorder_route)
    traverse_postorder(root, nodeinfo, postorder_route)
    return [preorder_route, postorder_route]

# 입력 예
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result = solution(nodeinfo)
print(result)
