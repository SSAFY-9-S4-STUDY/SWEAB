import sys
sys.stdin = open('4466.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int,input().split())
    scores = sorted(list(map(int, input().split())), reverse = True)

    print(f'#{test_case} {sum(scores[:K])}')