from collections import deque

N, L, R = map(int, input().split())

# 2차 배열을 만드는 과정
group = []
for _ in range(N):
    group.append(list(map(int, input().split())))

# BFS로 풀거임.
queue = deque()

# 델타 방향
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

status = False
ans = 0

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    team = []
    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                queue.append((j, i))
                visited[j][i] = 1
                team.append((j, i))

                while queue:
                    now = queue.popleft()

                    for k in range(4):
                        ny, nx = now[0] + dy[k], now[1] + dx[k]

                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                            if L <= abs(group[now[0]][now[1]] - group[ny][nx]) <= R:
                                queue.append((ny, nx))
                                team.append((ny, nx))
                                visited[ny][nx] = 1

                if len(team) > 1:  # 이렇게 한 이유는 항상 자기 자신은 포함되기에 그를 제외한 팀원이 있는지 찾기 위함입니당
                    status = True

                    after_move = sum(map(lambda x:group[x[0]][x[1]], team)) // len(team)

                    for point in team: group[point[0]][point[1]] = after_move
                    team.clear()  # 다음 경우를 위해서 비워줘야 해요

                else:
                    team.clear()  

    if not status:
        break

    ans += 1
    status = False

print(ans)