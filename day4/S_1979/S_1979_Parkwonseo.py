T = int(input())
for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    
    puzzle = []
    for one_line in range(N):
        puzzle.append(input().split())
    
    result = 0
    for y in range(N):
        count = 0
        for x in range(N):
            if puzzle[y][x] == "1":
                count += 1
                if count == K:
                    result += 1
                elif count == K + 1:
                    result -= 1
            else:
                count = 0

    for x in range(N):
        count = 0
        for y in range(N):
            if puzzle[y][x] == "1":
                count += 1
                if count == K:
                    result += 1
                elif count == K + 1:
                    result -= 1
            else:
                count = 0
                
    print(f'#{test_case} {result}')

# loop를 한번만 돌려 1을 찾고 거기서 시작해볼까