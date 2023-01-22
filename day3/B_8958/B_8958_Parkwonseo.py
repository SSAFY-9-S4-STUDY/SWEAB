T = int(input())
# for test_case in range(1, T + 1):
    
#     quiz = input()
    
#     score_board = []
#     tmp = []
#     for idx, ox in enumerate(quiz):
#         if ox == 'O':
#             tmp.append(ox)
#             if idx == len(quiz) - 1:
#                 score_board.append(tmp)    
#         else:
#             if tmp != []: score_board.append(tmp)
#             tmp = []
    
#     score = 0
#     for i in range(len(score_board)):
#         for j in range(len(score_board[i])):
#             score += (j + 1)

for t in range(0, T):
    quiz = input()
    tmp = 0
    score = 0
    for ox in quiz:
        if ox == 'O':
            tmp += 1
        else:
            tmp = 0
        score += tmp

    print(score)