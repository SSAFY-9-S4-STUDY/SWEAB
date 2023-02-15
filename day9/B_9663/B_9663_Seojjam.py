import sys
input = sys.stdin.readline

N = int(input())
cnt = 0  # N-Queen 개수

for j in range(N):
    chess = [[0] * N for _ in range(N)]
    start_i, start_j = 0, j
    # 스택에 좌표 추가
    stack = [(start_i, start_j)]

    # 반복범위 : 스택이 빌 때 까지
    while stack:
        print(stack)
        # 스택에서 좌표를 뽑기
        new_i, new_j = stack.pop()

        # Queen의 공격가능 좌표 1 처리
        for k in range(N):
            chess[new_i][k] = 1  # 행 1 처리
            chess[k][new_j] = 1  # 열 1 처리
            if new_i + k < N and new_j + k < N:  # 대각 1 처리
                chess[new_i + k][new_j + k] = 1
            if new_i + k < N and 0 <= new_j - k:  # 역대각 1 처리
                chess[new_i + k][new_j - k] = 1

        # 마지막 줄이 아니면
        if new_i < N - 1:
            new_i += 1  # 1열 내려와서 j값 검사
        else: break

        for r in range(N):
            # 좌표값이 0이면 스택에 추가
            if not chess[new_i][r]:
                stack.append((new_i, r))
                if new_i == N - 1: cnt += 1
            # 좌표값이 1이면 넘어가~
            else: continue
        # for문 끝나면 다음 j에서 같은 과정 반복
        else: continue
    # while문 끝나면 다른 점에서 while문 start
    else: continue

print(cnt)






