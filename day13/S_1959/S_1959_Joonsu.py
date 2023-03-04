import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    if N > M:
        longer = list(map(int, input().split()))
        shorter = list(map(int, input().split()))
    else:
        shorter = list(map(int, input().split()))
        longer = list(map(int, input().split()))

    trial = len(longer) - len(shorter) + 1
    results = [0] * trial
    for i in range(trial):
        for j in range(len(shorter)):
            results[i] += shorter[j] * longer[i+j]

    print(f'#{test_case} {max(results)}')