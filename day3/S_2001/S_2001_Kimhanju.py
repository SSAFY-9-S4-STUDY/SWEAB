import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T + 1):

    N,M = map(int,input().split())

    spaces = []
    for _ in range(N):
        spaces.append(list(map(int,input().split())))
    
    flys = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            for m in range(M):
                sum_fly += sum(spaces[i+m][j:j+M])
            flys.append(sum_fly)
    print(f'#{test_case} {max(flys)}')