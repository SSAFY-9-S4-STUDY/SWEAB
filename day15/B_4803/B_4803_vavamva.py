# 트리
# import pprint

tc = 0
while True:
    tc += 1
    nodes, edges = map(int, input().split())

    if (nodes, edges) == (0, 0):
        break

    visited = [0] * (nodes + 1)
    link = [[0] * (nodes + 1) for _ in range(nodes + 1)]

    for _ in range(edges):
        node_1, node_2 = map(int, input().split())

        link[node_1][node_2] = 1
        link[node_2][node_1] = 1
    # print("initial")
    # pprint.pprint(link)
    tree_num = 0
    for node in range(1, nodes + 1):

        if visited[node] == 0:
            stack = [node]
            flag = True
            # t = 0
            while stack:
                # t += 1
                # print(f"#{t, stack}")
                now = stack.pop()
                if visited[now] == 0:
                    visited[now] = 1
                    for idx in range(1, nodes + 1):
                        if link[now][idx] == 1 and idx in stack:
                            flag = False
                            link[now][idx] = 0
                            link[idx][now] = 0
                        elif link[now][idx] == 1:
                            stack.append(idx)
                            link[now][idx] = 0
                            link[idx][now] = 0
                    # print(f"@@{now}")
                    # pprint.pprint(link)

            # print(f"##{t, flag}")
            if flag:
                tree_num += 1

    if tree_num > 1:
        print(f"Case {tc}: A forest of {tree_num} trees.")
    elif tree_num == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: No trees.")