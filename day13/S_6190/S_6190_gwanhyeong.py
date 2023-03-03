# idea : i, j(i < j) 에 대해 arr[i] 와 arr[j]를 곱해서
# 문자열로 바꾸고 각 자리를 비교하여 단조증가하는지 확인 후
# for문을 다 돌면 단조증가하는 수이므로 기존 ans와 비교하여 더 큰 값을 ans 변수에 할당

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = -1
    for i in range(N):
        for j in range(i+1, N):
            check = arr[i] * arr[j]
            check_str = str(check)
            for k in range(1, len(check_str)):
                if int(check_str[k]) < int(check_str[k-1]):
                    break
            else:
                if check > ans:
                    ans = check
    print(f'#{tc} {ans}')