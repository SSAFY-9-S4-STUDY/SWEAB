# idea : 돈 액수를 리스트에 넣고 해당 인덱스에 해당하는 빈 리스트 생성
# while 반복문으로 각 액수에 대해 count 해준다.

import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1,t+1):
    N = int(input())
    temp_list = [0] * 8
    money_list = [50000,10000,5000,1000,500,100,50,10]
    for i in range(8):
        while N >= money_list[i]:
            temp_list[i] += 1
            N -= money_list[i]
    print(f'#{tc}')
    print(*temp_list)