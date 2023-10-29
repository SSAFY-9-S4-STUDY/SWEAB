def nodeinfo2tree(nodeinfo):
    tree = dict()
    print(nodeinfo)

    for idx, [cx, cy, cnum] in enumerate(nodeinfo):
        tree[cnum] = []
        parentIdx = idx - 1

        if parentIdx < 0:
            continue

        while nodeinfo[parentIdx][1] == cy:
            parentIdx -= 1

        tree[nodeinfo[parentIdx][2]].append(cnum)

        print(tree)

    return tree


def solution(nodeinfo):
    answer = []

    # 0. nodeinfo에 노드번호 저장
    for idx in range(len(nodeinfo)):
        nodeinfo[idx].append(idx + 1)

    # 1. y-x 순 nodeinfo 정렬
    nodeinfo.sort(key=lambda node: (-node[1], node[0]))

    # 2. 트리 만들기
    tree = nodeinfo2tree(nodeinfo)

    # 3. 전위 순회

    # 4. 후위 순회

    return answer


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)
