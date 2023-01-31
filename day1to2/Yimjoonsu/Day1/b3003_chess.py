chess_num = [1, 1, 2, 2, 2, 8]
chess_found = list(map(int,input().split()))

for i in range(6):
    print(chess_num[i] - chess_found[i])