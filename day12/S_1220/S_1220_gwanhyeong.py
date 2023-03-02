# Idea : 열을 기준으로 행을 쭉 탐색
# 1이 먼저 나오고 2가 나오면 교착상태 발생하므로 스택 이용
for tc in range(1, 11):
    # 배열의 한 변의 길이
    N = int(input())
    # 배열 입력
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 교착 상태의 개수를 변수 cnt에 할당
    cnt = 0

    # 열 탐색(0~N-1)
    for i in range(N):
        # 열마다 스택을 초기화해주어야 함
        stack = []
        for j in range(N):
            # 1을 만나면 스택에 1을 추가
            if arr[j][i] == 1:
                stack.append(1)
            # 2를 만나면 스택이 비어있지 않다는 건 1이 있다는거니까
            # 교착 상태 개수 + 1
            # 그리고 스택 비워줌
            elif arr[j][i] == 2:
                if stack:
                    cnt += 1
                    stack = []

    print(f'#{tc} {cnt}')