from collections import deque

def solution(n, k, cmd):
    # 이동 시 가게 될 왼쪽, 오른쪽 인덱스 번호 (-1 : 여기가 끝 행임을 의미)
    # deleted : 삭제된 행 정보
    linked = [[-1,1]] + [[i-1, i+1] for i in range(1, n-1)] + [[n-2,-1]]
    deleted = deque([])
    # 커맨드를 따라 표편집 진행
    for c in cmd:
        # 삭제 커맨드
        if c == 'C':
            # deleted에 행 정보 추가하고 삭제
            left, right = linked[k]
            deleted.append((left, right, k))
            linked[k] = 0
            # linked 수정
            if left > -1: linked[left][1] = right
            if right > -1: linked[right][0] = left
            # k 수정
            k = right if right > 0 else left
            move = 0
        # 되돌리기 커맨드
        elif c == 'Z':
            left, right, row = deleted.pop()
            # linked에 삭제된 행 추가
            linked[row] = [left, right]
            # 좌우 연결 정보 수정=
            if left > -1: linked[left][1] = row
            if right > -1: linked[right][0] = row
        # 이동 커맨드
        else:
            updown, move = c.split()
            move = int(move)
            # d: direction => 이동시 linked에서 하위 리스트에서 선택하게될 인덱스
            d = 0 if updown == 'U' else 1 
            # 이동
            for _ in range(abs(move)):
                k = linked[k][d]

    # 반환값 조건에 맞게 변형
    return ''.join(map(lambda x: 'O' if x else 'X', linked))

n, k = 8, 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))