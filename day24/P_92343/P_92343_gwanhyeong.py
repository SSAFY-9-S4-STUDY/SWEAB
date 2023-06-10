from collections import deque
def solution(info, edges):
    n = len(info)
    tree = [[] for _ in range(n)]
    answer = 1  # 루트 노드는 양으로 고정됨.
    
    for p, c in edges:
        tree[p].append(c)
    
    # deque(Double Ended Queue)는 양쪽 끝을 모두 추출할 수 있는 큐를 일반화한 형태
    # pop(), popleft() 모두 시간복잡도 O(1)을 가지므로 성능이 좋다.
    q = deque([[tree[0], 1, 1]])

    while q:
        data = q.popleft()

        for i, next_node in enumerate(data[0]):
            # total 변수에는 그동안 모은 양의 개수
            total = data[2]
            # next_node가 양이라면 temp 변수에 양의 수 - 늑대의 수 + 1 할당하고 total +=1
            if info[next_node] == 0:
                temp = data[1] + 1
                total += 1
            # next_node가 늑대라면 temp 변수에 양의 수 - 늑대의 수 - 1 할당
            else:
                temp = data[1] - 1
            # temp 변수, 즉 양의수-늑대수가 0 초과인 경우 해당 노드를 방문했으니 data[0]에서 i번째를 제외한 나머지 노드들과 바뀐 temp, total 변수를 deque에 append
            if temp > 0:
                q.append([data[0][:i] + data[0][i+1:] + tree[next_node], temp, total])
                # answer과 total 비교하여 answer이 더 크다면 갱신
                answer = max(answer, total)
    
    return answer