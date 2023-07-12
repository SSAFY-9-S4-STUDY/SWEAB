from collections import deque

def solution(board, row, col):
    # 좌표간 최단 거리 찾기 함수
    def shortest(r1, c1, r2, c2):
        # 좌표별 최단 거리를 기록할 이중배열
        visited, queue = [[99]*4 for _ in range(4)], deque([(r1, c1)])
        visited[r1][c1] = 0
        # bfs와 dp로 최단거리를 visited에 기록
        while queue:
            r, c = queue.popleft()
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc, o, end = r+x, c+y, 1, False
                while 0 <= nr < 4 and 0 <= nc < 4:
                    if nr in [0,3] or nc in [0,3] or board[nr][nc]:
                        o, end = 1, True
                    if visited[r][c] + o < visited[nr][nc]:
                        queue.append((nr,nc))
                        visited[nr][nc] = visited[r][c] + o
                    if end: break
                    nr, nc, o = nr + x, nc + y, o + 1
                    
        return visited

    # cards_loc = {i:[] for i in range(1, 9)}
    # for r in range(4):
    #     for c in range(4):

    # total, answer = (16-sum(board, []).count(0))//2, 9999
    print()
    return shortest(0, 0, 3, 2)

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))