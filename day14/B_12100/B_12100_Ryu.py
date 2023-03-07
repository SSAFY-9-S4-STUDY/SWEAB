import sys
sys.stdin = open('2048.txt')

input = sys.stdin.readline

size = int(input())
lst = [list(map(int, input().split())) for i in range(size)]
temp = [[0 for i in range(size)] for j in range(size)]

# 사이에 그것들을 어떻게 저장할 것인가는 없는 것이다.


def move(a): # 상하좌우 + 최대값 뽑아내야한다.
    global temp, size

    rlt = 0
    if a == 0:  # 위로 움직이기
        for j in range(size):
            prev = 0
            order = 0
            for i in range(size):

                if prev != 0 and prev == temp[i][j]:
                    temp[order - 1][j] *= 2
                    prev = 0
                else:

                    if temp[i][j] != 0:
                        prev = temp[i][j]
                        temp[order][j] = temp[i][j]
                        order += 1
            for i in range(order, size):
                temp[i][j] = 0

    elif a == 1:  # 아래로 움직이기
        for j in range(size):
            prev = 0
            order = size - 1
            for i in range(size - 1, -1, -1):

                if prev != 0 and prev == temp[i][j]:
                    temp[order + 1][j] *= 2
                    prev = 0
                else:

                    if temp[i][j] != 0:
                        prev = temp[i][j]
                        temp[order][j] = temp[i][j]
                        order -= 1
            for i in range(order + 1):
                temp[i][j] = 0


    elif a == 2:  # 왼쪽로 움직이기
        for i in range(size):
            prev = 0
            order = 0
            for j in range(size):

                if prev != 0 and prev == temp[i][j]:
                    temp[i][order - 1] *= 2
                    prev = 0
                else:

                    if temp[i][j] != 0:
                        prev = temp[i][j]
                        temp[i][order] = temp[i][j]
                        order += 1
            for j in range(order, size):
                temp[i][j] = 0


    elif a == 3:  # 오른쪽로 움직이기
        for i in range(size):
            prev = 0
            order = size - 1
            for j in range(size - 1, -1, -1):

                if prev != 0 and prev == temp[i][j]:
                    temp[i][order + 1] *= 2
                    prev = 0
                else:

                    if temp[i][j] != 0:
                        prev = temp[i][j]
                        temp[i][order] = temp[i][j]
                        order -= 1
            for j in range(order + 1):
                temp[i][j] = 0



max_num = 0
num = 1024
for i in range(num):
    move_lst = []
    now_max = 0
    for j in range(5):
        move_lst.append(i % 4)
        i //= 4

    for a in range(size):
        for b in range(size):
            temp[a][b] = lst[a][b]

    for a in range(5):
        move(move_lst[a])
        #여기에 백트래킹 들어간다, 움직이지 않는 경우의 수도? 응 백트래킹하면 안된다

    for i in range(size):
        for j in range(size):
            if temp[i][j] > max_num:
                max_num = temp[i][j]

print(max_num)
