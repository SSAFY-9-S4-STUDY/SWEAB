from collections import deque

# M : 상자의 가로칸, N : 상자의 세로칸, tomato : 토마토 판
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# 방향설정, 정답을 담아줄 ans설정 -1인 이유는 처음부터 다 익은경우 0 출력하기 편하라고
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = -1

# 초기상태에서 토마토가 익어있는경우 좌표를 큐에 담아줌
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i,j))

while queue:
    ans +=1
    # 큐에 존재하는 인자의 수 만큼 돌려줌 
    # 다 돌면 그 다음 일차
    for _ in range(len(queue)):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1
                    queue.append([nx,ny])

# 끝났는데 안익은 토마토가 있으면 -1
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            ans = -1

print(ans)