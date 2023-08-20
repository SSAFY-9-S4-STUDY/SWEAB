from collections import deque

def solution(board):
    # 1. 변수 설정
    # 미로 크기
    N = len(board) 
    # 각 칸 당 최저 
    min_cost_arr = [[float("inf")] * N for _ in range(N)]  

    # 2. bfs와 dp를 위한 초기값 세팅
    # 시작 지점 코스트 -500(시작지점에서 이동할 때 코너가 있다고 판단해버리기 때문)
    min_cost_arr[0][0] = -500
    # bfs를 위한 큐 - 배열 안 요소는 (행, 열, 방향)
    # 방향 - 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    Q = deque([(0,0,0), (0,0,1)])

    # 3. bfs를 dp 시행
    dirs = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    while Q:
        row, col, dir = Q.popleft()
        for d in range(4):
            nrow, ncol = row + dirs[d][0], col + dirs[d][1]
            
    #         # 벽이 있는 위치거나 배열 밖으로 벗어나면 탐색 X
    #         if nrow < 0 or nrow > N-1: continue
    #         if ncol < 0 or ncol > N-1: continue
    #         if board[nrow][ncol]: continue
    #         # 코너 여부를 판단하여 비용 계산
    #         cost = 100 if dir == d else 600
    #         total_cost = min_cost_arr[row][col] + cost
    #         # 현재까지의 비용이 이동 지점에 기록된 비용보다 적다면 계속해서 탐색
    #         if total_cost < min_cost_arr[nrow][ncol]:
    #             min_cost_arr[nrow][ncol] = total_cost
    #             Q.append((nrow, ncol, d))

    # return min_cost_arr


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))