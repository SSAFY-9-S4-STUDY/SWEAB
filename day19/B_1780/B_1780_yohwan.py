import sys
sys.stdin = open("input.txt")

# 종이 자르는 함수
def cut(x, y, N):
    global minus, zero, plus
    check = paper[x][y]
    
    # range(N)이 아닌 x ~ x+N인 이유: 시작점을 계속 3분할 해주기 위함
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != check:
                # 여기가 종이 9등분해서 다시 cut돌리는 과정
                for k in range(3):
                    for l in range(3):
                        cut(x+k*N//3, y+l*N//3, N//3)
                return
    
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
minus = 0
zero = 0
plus = 0

cut(0, 0, N)
print(minus)
print(zero)
print(plus)