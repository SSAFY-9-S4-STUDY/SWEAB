# 최소 노드 경로..
def solution(_board, r, c):
    global board, pairs
    board = _board
    answer = 0
    print(bfs(r, c))

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
    return r, c


# pair 찾기 함수
def bfs(r, c):
    q = set()
    q.add((r, c))
    distance = [[16 for _ in range(4)] for _ in range(4)]
    distance[r][c] = 0  # 시작점 표시
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    target = board[r][c]
    print('target: ', target)

    while q:
        r, c = q.pop()

        for dr, dc in dirs:
            r1, c1 = r + dr, c + dc
            r2, c2 = ctrl_move(r, c, dr, dc)

            if not is_in(r1, c1) or (r, c) == (r2, c2):
                continue

            if board[r1][c1] == target:
                print('도착1: ', board[r1][c1])
                board[r1][c1] = 0
                return distance[r][c] + 1

            elif board[r2][c2] == target:
                print('도착2: ', board[r2][c2])
                board[r2][c2] = 0
                return distance[r][c] + 1

            else:
                if distance[r1][c1] > distance[r][c] + 1:
                    distance[r1][c1] = distance[r][c] + 1
                    q.add((r1, c1))
                if distance[r2][c2] > distance[r][c] + 1:
                    distance[r2][c2] = distance[r][c] + 1
                    q.add((r2, c2))

        print(distance)

    board[r][c] = 0


solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)

# print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
# print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))