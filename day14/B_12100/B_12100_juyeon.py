# 시간 부족으로 최적화는 못함,, 코드 더 줄일 수 있는 방안 있을듯 초안에 풀고 검토토 못함 ㅜ_ㅜ 



import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)


def rev(a):
    a_rev = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a_rev[i] = a[i][::-1]
    return a_rev

def rotation_clock(a): # 시계방향 회전
    a_rot = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            a_rot[i][j] = a[N-1-j][i]

    return a_rot    

def rotation_cnt_clock(a): # 반시계방향 회전
    a_rot = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a_rot[j][i] = a[i][N-1-j]
    return a_rot    

def left(a):
    a_left = [[] for _ in range(N)]
    for i in range(N):
        stack = [0]*N
        top = -1
        idx = -1
        for j in a[i]:
            if j and idx >= top:
                top += 1 
                stack[top] = j
            elif j and idx < top:
                if stack[top] == j:
                    # print(top, idx)
                    stack.pop(top)
                    stack += [0]
                    stack[top] = j * 2
                    idx = top
                elif stack[top] != j:
                    top += 1 
                    stack[top] = j                    
        a_left[i] = stack
    return a_left

def right(a):
    return rotation_clock(rotation_clock(left(rotation_clock(rotation_clock(a)))))

def up(a):
    return rotation_clock(left(rotation_cnt_clock(a)))
    
def down(a):
    return rotation_cnt_clock(left(rotation_clock(a)))

def DFS(arr):
    global res, a, max_sum, jy

    funtions = [left, right, up, down]
    if res == 5:
        max_sum_local = max(sum(arr,[]))
        if max_sum_local > max_sum:
            max_sum = max_sum_local
            jy.append(max_sum)

    elif res < 5:
        for i in funtions:
            _arr = i(arr)
            res += 1
            DFS(_arr)
            res -= 1

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
res = 0

max_sum = 0
jy =[]
DFS(board)
print(max(jy))