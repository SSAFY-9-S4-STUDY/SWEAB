import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    length, squat = map(int, input().split())
    sq = []
    for i in range(0, length):
        sq.append(list(map(int, input().split())))
    
    squatted  = 0
    for j in range(length - squat + 1):
        for k in range(length - squat + 1):
            dead_fly  = 0
            for l in range(j, j + squat):
                for m in range(k, k + squat):
                    dead_fly += sq[l][m]
            if dead_fly > squatted:
                squatted = dead_fly
                
    print(f'#{test_case} {squatted}')