# from collections import defaultdict
#
#
# def solution(_board, r, c):
#     answer = 0
#     global board
#     board = _board
#
#      # [1] 짝 위치 기억해두기
#     pairs = defaultdict(list)
#     for i in range(4):
#         for j in range(4):
#             if board[i][j]:
#                 pairs[board[i][j]].append((i, j))
#
#     # [2] 이동하기
#     print(get_cnt((1,0), (2,3), 0))
#
#     return answer
#
#
# def is_in(r, c):
#     if r < 0 or 3 < r or c < 0 or 3 < c:
#         return False
#     return True
#
#
# def get_cnt(now, target, cnt):
#     dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#     max_cnt = 4
#
#     if cnt >= max_cnt:
#         return
#
#     if now == target:
#         return min(cnt, max_cnt)
#
#     r, c = now
#     for dr, dc in dirs:
#         get_cnt((r+dr, c+dc), target, cnt+1)
#         get_cnt(ctrl_move(r, c, dr, dc), target, cnt+1)
#
#
# def ctrl_move(r, c, dr, dc):
#     while is_in(r+dr, c+dc) and not board[r+dr][c+dc]:
#         r, c = r + dr, c + dc
#     return r, c

#
# def move(r, c, tr, tc):
#     cnt = 1
#
#     if r == tr:
#         if tc < c:  # 좌
#
#         else:       # 우
#             pass
#     elif c == tc:
#         if tr < r:  # 상
#             pass
#         else:       # 하
#             pass
#     elif tr < r:
#         if c < tc:  # 1사분면
#             pass
#         else:       # 2사분면
#             pass
#     else:
#         if tc < c:  # 3사분면
#             pass
#         else:       # 4사분면
#             pass



def solution(board, r, c):
    answer = 0
    return answer




print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))