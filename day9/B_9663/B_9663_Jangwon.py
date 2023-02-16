####################################
# 오늘(2/16) 공부하고 다시 올릴게요...! #
# 아래에는 실패한 코드...ㅠㅠㅠ 하...ㅠ  #
####################################

import sys
sys.stdin = open('input.txt')

n = int(input())

# 선택한 거 표시하기 위한...(열 날리기)
route = list()
done = list()

# 대각선을 날리기 위한( 규칙 반영[왼쪽은 왼대각] [오른쪽은 오른 대각])
visited = [[], []]


def left_diag(a):
    return a[0] - a[1]


def right_diag(a):
    return a[0] + a[1]


# 시작
start = [0, 0]  # [y, x]
route.append(start)
cnt = 0


def look_around(start):
    global cnt
    # 백트래킹(1)
    if not route:
        return
    # 방향설정(8방향 설정)
    dy = [0, 1, 0, -1, 1, 1, -1, -1]
    dx = [1, 0, -1, 0, 1, -1, -1, 1]

    if start not in visited:
        done.append(start)
        visited[0].append(left_diag(start))
        visited[1].append(right_diag(start))

    if len(done) >= n:
        cnt +=1
        return
    for i in range(8):
        for t in range(n):
            next = [start[0] + dy[i] * t, start[1] + dx[i] * t]
            if (0 <= next[0] < n and 0 <= next[1] < n) and next[1] != start[1] and next[0] != start[0] \
                    and left_diag(next) not in visited[0] and right_diag(next) not in visited[1]:
                route.append(next)

    look_around(route.pop())

    return cnt


print(look_around(start))
