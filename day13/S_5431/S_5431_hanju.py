import sys
sys.stdin = open('5431.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    hw = list(map(int,input().split()))
    students = filter(lambda x: x not in hw, list(range(1, N+1)))
    print(f'#{test_case}', *list(students))