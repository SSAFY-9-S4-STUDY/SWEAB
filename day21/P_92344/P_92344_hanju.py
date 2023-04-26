def solution(board, skill):
    N, M  = len(board), len(board[0])
    # 변화량을 기록할 이중배열
    changes = [[0]*(M+1) for _ in range(N+1)]
    # 네 꼭지점에 변화량을 기록
    for t, r1, c1, r2, c2, d in skill:
        value = d * ((-1)**t)
        changes[r1][c1] += value
        changes[r2+1][c2+1] += value
        changes[r1][c2+1] -= value
        changes[r2+1][c1] -= value
    # 변화량을 기록하며 건물 HP 측정
    changes = [[0]*(M+1)] + changes
    ans = 0
    for r in range(N):
        change = 0
        # 직전 행의 변화를 현재 행에도 반영
        # 오른쪽으로 가면서 변화량을 갱신
        for c in range(M):
            changes[r+1][c] += changes[r][c]
            change += changes[r+1][c]
            # board에 변화량을 적용한 값이 양수면 ans에 + 1
            if board[r][c] + change > 0:
                ans += 1
    return ans

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))

