import sys
sys.stdin = open('1220.txt', 'r')


for test_case in range(1, 11):
    N = int(input())

    magnetics = [list(input().split()) for _ in range(N)]
    magnetics = list(zip(*magnetics))

    total = 0
    for m in magnetics:
        tmp = ''.join(m)
        tmp = tmp.replace('0', '').replace(' ','')
        total += tmp.count('12')

    print(f'#{test_case} {total}')