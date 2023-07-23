from collections import deque
from itertools import permutations
from copy import deepcopy

board_v = []

def solution(board, r, c):
    global board_v
    location = [[] for _ in range(7)]   # 각 카드별 위치
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                location[board[i][j]].append((i, j))
                if board[i][j] not in nums:
                    nums.append(board[i][j])
    
    per = list(permutations(nums, len(nums))) # 순열
    # print(per)
    answer = 100

    for i in range(len(per)):
        board_v = deepcopy(board) # 지웠던 곳 다시 채우기
        cnt = 0
        tmp_r, tmp_c = r, c
        
        # 먼저 지울 카드 순서
        for j in per[i]:
            # 왼쪽에 있는 것부터 제거했을 때 조작 횟수
            left = bfs((tmp_r, tmp_c), location[j][0])
            # 오른쪽에 있는 것부터 제거했을 때 조작 횟수
            right = bfs((tmp_r, tmp_c), location[j][1])
            if left < right:
                cnt += left
                cnt += bfs(location[j][0], location[j][1])
                tmp_r, tmp_c = location[j][1]
            else:
                cnt += right
                cnt += bfs(location[j][1], location[j][0])
                tmp_r, tmp_c = location[j][0]
            board_v[location[j][0][0]][location[j][0][1]] = 0
            board_v[location[j][1][0]][location[j][1][1]] = 0
            cnt += 2 # enter
        answer = min(answer, cnt)
    return answer


def ctrl_move(tmp_r, tmp_c, dr, dc):
    global board_v
    nxt_r, nxt_c = tmp_r, tmp_c
    while True:
        nr = nxt_r + dr
        nc = nxt_c + dc
        if not (0<=nr<4 and 0<=nc<4):
            return nxt_r, nxt_c
        # 다른 카드를 만나면 멈춤
        if board_v[nr][nc] != 0:
            return nr, nc
        nxt_r = nr
        nxt_c = nc

def bfs(start, end):
    init_r, init_c = start
    find_r, find_c = end
    queue = deque()
    queue.append((init_r, init_c, 0))
    visited = [[0]*4 for _ in range(4)]
    move = [(0,-1),(0,1),(-1,0),(1,0)]
    while queue:
        init_r, init_c, temp = queue.popleft()
        if visited[init_r][init_c]:
            continue
        visited[init_r][init_c] = 1
        if init_r == find_r and init_c == find_c:
            return temp
        
        for dr, dc in move:
            nxt_r = init_r + dr
            nxt_c = init_c + dc
            if 0<=nxt_r<4 and 0<=nxt_c<4:
                queue.append((nxt_r,nxt_c, temp+1))
            nxt_r, nxt_c = ctrl_move(init_r, init_c, dr, dc)
            queue.append((nxt_r, nxt_c, temp+1))
    return -1


print('#1', solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print('#2', solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))