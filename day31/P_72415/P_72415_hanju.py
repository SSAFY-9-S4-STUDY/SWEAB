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
                # 배열의 끝이거나 캐릭터가 있는 칸에 도달하면 그 방향 탐색 종료
                while 0 <= nr < 4 and 0 <= nc < 4:
                    if nr+x in [-1,4] or nc+y in [-1,4] or board[nr][nc]:
                        o, end = 1, True
                    if visited[r][c] + o < visited[nr][nc]:
                        queue.append((nr,nc))
                        visited[nr][nc] = visited[r][c] + o
                    if end: break
                    nr, nc, o = nr + x, nc + y, o + 1
        return visited[r2][c2]


    # dfs를 통해 짝이 맞는 카드를 찾는 함수
    def find_pair(remain, o, s, e):
        nonlocal ans
        # 기록된 최소 조작수보다 크다면 종료
        if o >= ans: return
        # 남은 카드가 없다면 최소값 갱신
        if not remain: ans = o
        # 처음 뒤집을 카드를 선택
        for n in range(1,7):
            # 아직 남아있는 카드가 아니라면 넘김
            if not card_exist[n]: continue
            # 아니라면 두 짝 순서를 바꾸어가며 탐색
            first, second = cards_locs[n]
            f_s, s_f = shortest(first[0], first[1], second[0], second[1]), shortest(second[0], second[1], first[0], first[1])
            go_first, go_second = shortest(s, e, first[0], first[1]), shortest(s, e, second[0], second[1])
            card_exist[n], board[first[0]][first[1]], board[second[0]][second[1]] = 0, 0, 0
            find_pair(remain-1, o + f_s + go_first + 2, second[0], second[1])
            find_pair(remain-1, o + s_f + go_second + 2, first[0], first[1])
            card_exist[n], board[first[0]][first[1]], board[second[0]][second[1]] = 1, n, n


    # 카드들의 위치 파악
    cards_locs, card_exist = {i:[] for i in range(7)}, [0 for i in range(7)]
    for r in range(4):
        for c in range(4):
            tmp = board[r][c]
            cards_locs[tmp].append((r,c))
            card_exist[tmp] = 1

    # 답 구하기
    ans = 1000
    find_pair(sum(card_exist)-1, 0, row, col)
    return ans

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))