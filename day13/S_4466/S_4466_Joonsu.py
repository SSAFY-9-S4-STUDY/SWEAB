T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    score = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    for i in range(K):
        result += score[i]
    print(f'#{test_case} {result}')