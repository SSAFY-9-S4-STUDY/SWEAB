import sys
sys.stdin = open('4858.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst_num = sorted(list(map(int,input().split())))
    print(f'#{test_case} {lst_num[N-1]-lst_num[0]}')