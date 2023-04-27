from collections import deque

def solution(n, k, cmds):
    # 현재 남아있는 행 개수와 행 번호
    remain, row = n-1, k
    # 배열에서의 위치와 이동할 거리 표시
    loc, move = 1, k
    # 커맨드에 따른 이동 방향을 나타내기 위한 딕셔너리
    direction = {'D': 1, 'U': -1}
    # 현재 상태를 표현할 배열들
    group = [0, n] + ['O']*(n-2) + [1, 0]
    deleted = deque()
    # 커맨드에 따라 연산 진행
    for cmd in cmds:
        # 삭제 커맨드
        if cmd == 'C':
            # 이동 방향 결정
            dir = 1 if move > 0 else -1
            # 이동
            while move:
                # 현재 위치가 지워져있으면 위치 한 칸 이동
                if not group[loc+dir]:
                    loc += dir
                    continue
                # 현재 위치가 그룹 한 중간일 경우
                if group[loc] and not group[loc]


            # row와 remain 갱신
            # 끝 행을 지웠을 경우 행 위치 한 칸 올려줌
            remain -= 1
            if row > remain: row -= 1
        # 되돌리기 커맨드
        elif cmd == 'Z':
            comeback = deque.pop()
            # 되돌린 요소가 속한 그룹의 시작 인덱스와 끝 인덱스 갱신
            s = group[comeback-1] if group[comeback-1] else comeback
            e = group[comeback+1] if group[comeback+1] else comeback
            group[comeback] = 'O'
            group[e], group[s] = s, e
            # row와 remain 갱신
            # 되돌린 행이 배열에서의 현재 위치보다 작으면 row + 1
            remain += 1
            if comeback < loc: row += 1
        # 이동 커맨드
        else:
            updown, distance = cmd.split(" ")
            distance = int(distance) * direction[updown]
            row += distance
            move += distance


    return group

n, k = 8, 2
cmds = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmds))