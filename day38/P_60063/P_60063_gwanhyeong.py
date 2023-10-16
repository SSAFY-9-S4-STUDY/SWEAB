from collections import deque

def candidate(cur1, cur2, new_board):
    Y, X = 0, 1
    cand = []
    DIR = [(-1,0),(1,0), (0,1),(0,-1)]
    for dy, dx in DIR:
        nxt1 = (cur1[Y] + dy, cur1[X]+dx)
        nxt2 = (cur2[Y] + dy, cur2[X]+dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
            cand.append((nxt1,nxt2))
        
        if cur1[Y] == cur2[Y]:
            UP, DOWN = -1, 1
            
    

def solution(board):
    N = len(board)
    new_board = [[1 for _ in range(N+2)] for _ in range(N+2)]
    
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    
     
    que = deque([(1, 1), (1, 2), 0])
    confirm = set([ ((1, 1), (1, 2)) ])

    # queue를 이용한 bfs
    while que:
        current_one, current_two, count = que.popleft()
        if current_one == (N, N) or current_two == (N, N):
            return count

    answer = 0
    return answer