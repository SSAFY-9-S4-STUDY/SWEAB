import sys
sys.stdin = open("input_1267.txt")

# 사이클 없음.
# 단방향 간선
# 자신의 parent node 에서 간선이 다 들어와야 작업 가능

for tc in range(1, 11):
    v, e = map(int, input().split())
    # 간선[짝수] -> 간선[홀수]
    link = list(map(int, input().split()))
    graph = [[] for _ in range(v + 1)]  # index = parent, value = child
    need = [0] * (v + 1)  # 부모 간선 몇개 존재하는지 표시해줄 리스트
    for i in range(e):
        graph[link[i * 2]].append(link[i * 2 + 1])
        need[link[i * 2 + 1]] += 1  # 자식간선이 호출된다 == 해당 node에는 부모간선이 존재한다.

    # dfs 탐색을 써야 부모 간선을 다 받으며 진행할 수 있을 것 같음
    stack = []
    for start in range(1, v + 1):
        if need[start] == 0:
            stack.append(start)

    visit_order = []  # 단방향 간선을 표시한 link로 표시한 것이므로, 그냥 순서만 받자
    while stack:
        now = stack.pop()
        visit_order.append(now)

        for next_v in graph[now]:
            if need[next_v] == 1:
                stack.append(next_v)
            else:  # 만약 need가 1개보다 많다면 (지금 한 작업 말고도 필요한 작업이 더 있다면)
                need[next_v] -= 1  # 하나 했다고 표시하고 넘어가기

    result = " ".join(map(str, visit_order))  # 요구하는 형식에 맞게 변환
    
    print(f"#{tc} {result}")
