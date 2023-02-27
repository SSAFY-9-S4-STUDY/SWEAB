import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 검색하기
    # 행(j): 0 -> N까지 수차적으로 검색
    for j in range(N):
        i = 0
        while i < N:
            # 0열 -> N열 순서로 검색해서 1이 나오면?
            if square[i][j] == 1:
                for k in range(i + 1, N):   # 1 밑에 2가 나올때까지 검색
                    if square[k][j] == 2:   # 2가 나오면?
                        ans += 1            # 교착상태 +1
                        i = k               # 2 바로 밑부터 다시 검색
                        break
                else:                       # 2가 안나오면?
                    break                   # break(교착될 수 없기 때문)
            i += 1

    print(f'#{tc} {ans}')