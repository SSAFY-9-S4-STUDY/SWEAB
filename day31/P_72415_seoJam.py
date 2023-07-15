# 최소 노드 경로..
def solution(_board, r, c):
    global board, pairs

    answer = 0
    board = _board
    pairs = list()

    for i in range(4):
        for j in range(4):
            # if (r, c) == (i, j):
            #     continue
            if board[i][j]:
                pairs.append((i, j))

    while pairs:
        # [1] 다음 카드로 이동
        dis_to = bfs(r, c)
        min_dis = 7
        nr, nc = -1, -1
        for i, j in pairs:
            if min_dis > dis_to[i][j]:
                min_dis = dis_to[i][j]
                nr, nc = i, j
        pairs.remove((nr, nc))
        answer += min_dis  # 이동거리
        print((nr, nc), answer)
        # [2] pair 카드로 이동
        answer += 1  # 시작 enter
        r, c = nr, nc
        # pair 카드 찾기
        for pair in pairs:
            if board[r][c] == board[pair[0]][pair[1]]:
                nr, nc = pair
                pairs.remove(pair)
                break
        answer += bfs(r, c)[nr][nc] + 1  # 이동거리 + 마침 enter
        board[r][c] = board[nr][nc] = 0  # 짝맞춘 카드 제거
        print((nr, nc), answer)
        print('-----------------')
    return answer


# board 안에 있는지 판단
def is_in(r, c):
    if r < 0 or 3 < r or c < 0 or 3 < c:
        return False
    return True


# ctrl + 방향키
def ctrl_move(r, c, dr, dc):
    while is_in(r+dr, c+dc) and not board[r+dr][c+dc]:
        r, c = r + dr, c + dc
    if is_in(r+dr, c+dc) and board[r+dr][c+dc]:
        r, c = r + dr, c + dc
    return r, c


# 최소 경로 찾기
def bfs(r, c):
    q = set()
    q.add((r, c))
    distance = [[16 for _ in range(4)] for _ in range(4)]
    distance[r][c] = 0  # 시작점 표시
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while q:
        r, c = q.pop()

        for dr, dc in dirs:
            r1, c1 = r + dr, c + dc
            r2, c2 = ctrl_move(r, c, dr, dc)

            if not is_in(r1, c1) or (r, c) == (r2, c2):
                continue

            if distance[r1][c1] > distance[r][c] + 1:
                distance[r1][c1] = distance[r][c] + 1
                q.add((r1, c1))

            if distance[r2][c2] > distance[r][c] + 1:
                distance[r2][c2] = distance[r][c] + 1
                q.add((r2, c2))

    return distance


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))