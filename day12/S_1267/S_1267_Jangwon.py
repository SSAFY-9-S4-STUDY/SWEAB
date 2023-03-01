from collections import deque
T = 10

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    V, E = map(int, input().split())
    queue = deque()
    # 이중리스트
    arr = [[] for _ in range(V + 1)]

    # 입력값 받기
    nlst = list(map(int, input().split()))

    # 조건부 방문지
    visited = [0 for _ in range(V + 1)]

    # 갈 수 있는 길 표시
    for i in range(E):
        arr[nlst[i * 2]].append(nlst[i * 2 + 1]) # 단방향 길 표시
        visited[nlst[i * 2 + 1]] += 1  # 일반적인 visited에 0으로 두는 것과 달리 방문을 몇 번 해야한다는 것을 visited에 두는 것.

    # BFS로 풀이를 할 생각
    # 시작점 찾기
    queue = []
    for i in range(1, V + 1):
        if visited[i] == 0:
            queue.append(i)

    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        for next in arr[now]:
            if visited[next] != 0:  # 0이 아니라는 것의 의미는 아직 그 수만큼 방문을 해야한다는 의미
                visited[next] -= 1  # 방문을 했기에 1을 빼준다. 이렇게 되면 만일 원래 2였다면 1이 되고 이 1의 의미는 아직 다른 노드를 통해서 방문 한 번 더해야 다음 노드로 넘어갈 수 있다는 의미.
                if visited[next] == 0: # 방문을 더 이상하지 않을 때 queue에 추가해준다.
                    queue.append(next)
    print()