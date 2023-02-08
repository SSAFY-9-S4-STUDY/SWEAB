"""
빈칸
n = 3 [0~2][0~2] : (1,1)

n = 9 [0~8][0~8] : (1,1) (4,1) (7,1)
                   (1,4) (3~5,3~5) (7,4)
                   (1,7) (4,7) (7,7)
"""


n = int(input())

def star(i, j, x):
    
    if x == 1:
        print("*", end= "")
        return
    elif (i // (x // 3)) % 3 == 1 and (j // (x // 3)) % 3 == 1:
        print(" ", end= "")
    else:
        star(i, j, x // 3)

for i in range(n):
    for j in range(n):
        star(i, j, n)
    print()
    
# python3 로 돌리면 시간초과
# pypy3 로 돌리니 pass