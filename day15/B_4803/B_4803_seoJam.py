import sys
sys.stdin = open("input.txt")

def dfs(pre, node):
    visited[node] = True
    for near in tree[node]:
        if pre == near:
            continue
        if visited[near]:
            return False
        if not dfs(node, near):
            return False
    return True

tc = 0
while True:
    tc += 1
    v, e = map(int, input().split())
    # [0] "0, 0" 입력되면 break
    if (v, e) == (0, 0):
        break
    tree = list([] for _ in range(v+1))
    visited = [0] * (v+1)
    answer = 0

    # [1] 트리 만들기
    for _ in range(e):
        v1, v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)

    # [2] dfs
    for node in range(1, v+1):
        if not visited[node]:
            if dfs(0, node):
                answer += 1

    if not answer:
        print(f'Case {tc}: No trees.')
    elif answer == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {answer} trees.')






