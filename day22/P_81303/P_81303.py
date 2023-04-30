# 구글링해서 공부했습니당...
def solution(n, k, cmd):
    # 현재 위치의 커서
    cur = k
    # 링크드 리스트를 딕셔너리로 만듬.
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []

    # cmd안에 있는 명령을 하나씩 보면서...
    for c in cmd:
        if c == "C":
            # 삭제
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])
            if next == None:  # 마지막에 위치
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:  # 맨 처음이라면
                table[next][0] = None  # 다음 위치의 prev를 None으로 할당
            elif next == None:  # 맨 마지막이라면
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev

        elif c == "Z":
            # 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'  # 다시 생김.
            if prev == None:  # 가장 첨이 돌아온다면
                table[next][0] = now  # 다음 위치에 있는 것의 prev를 now로 할당
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    return ''.join(answer)



#### 처음 풀이 ##
def solution(n, k, cmd):
    from collections import deque

    # 처음 정보 반영 구현
    row = list(range(n))  # 처음 행 상태
    now = k  # 현재 위치의 "인덱스"를 의미
    tmp_trash = deque()  # 지워질 경우 지워진 것을 담을 Stack

    # cmd 정의 dictionary
    def cmd_list(cmd, dist, pos):
        if cmd == "C":  # 현재 선택된 행 삭제 후, 바로 아래 행 선택
            tmp_trash.append(row.pop(pos))
            if pos == len(row):
                return len(row) - 1
            else:
                return pos
        elif cmd == "Z":  # 가장 최근에 삭제된 행을 원래대로 복구
            back = tmp_trash.pop()
            tmp = row[pos]
            row.insert(back, back)
            if back < tmp:
                return pos + 1
            else:
                return pos
        elif cmd == "U":  # 선택된 행에서 위에 있는 행을 선택
            if pos - dist >= 0:
                return pos - dist
            else:
                return 0
        else:  # 선택된 행에서 아래에 있는 행 서택
            if pos + dist < len(row):
                return pos + dist
            else:
                return len(row) - 1

    # 탐색 시작
    for c in cmd:
        step = c.split()
        if len(step) == 2:  # 방향을 옮기는 명령어
            now = cmd_list(step[0], int(step[1]), now)
        else:  # 지우거나 복구하는 명령어
            now = cmd_list(step[0], 0, now)

    # 최종 비교
    x = 0
    answer = ''
    while x < n:
        if x in row:
            answer += "O"
            x += 1
        else:
            answer += "X"
            x += 1
    return answer