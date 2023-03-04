T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # K는 선택 성적 수
    score_lst = list(map(int, input().split()))  # N개
    score_lst.sort(reverse=True)

    ans = sum(score_lst[:K])
    print(f'#{test_case} {ans}')