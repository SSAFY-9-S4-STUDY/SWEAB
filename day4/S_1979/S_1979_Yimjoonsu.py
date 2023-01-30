T = int(input())

def check(puzzle):
    count_row = 0
    count = 0

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                count_row += 1
            if (puzzle[i][j] == 0) or (j == N-1):
                if count_row == K:
                    count += 1
                count_row = 0
    return(count)

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [(list(map(int,input().split()))) for i in range(N)]
    print(f'#{test_case} {check(puzzle)+check(list(zip(*puzzle)))}')