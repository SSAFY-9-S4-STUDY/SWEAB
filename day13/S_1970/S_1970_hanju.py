import sys
sys.stdin = open('1970.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    change = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        tmp = money[i]
        money[i] = change // tmp
        change = change % tmp

    print(f'#{test_case}')
    print(*money)