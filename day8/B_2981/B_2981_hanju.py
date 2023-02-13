# 유클리드 호제법을 이용하여 최대 공약수 구하기
def gcd(lst, n):
    while n != 1:
        small = min(lst[:2])
        big = max(lst[:2])
        lst = lst[2:]
        while big % small != 0:
            big, small = small, big % small
        else:
            lst.append(small)
            n -= 1
    return lst[0]

import sys

N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])

sub_numbers = list(map(lambda x: x-numbers[0],numbers))[1:]
gcd_num = gcd(sub_numbers, N)

answer = [gcd_num]
for div in range(2, int(gcd_num**0.5) + 1):
    if gcd_num % div == 0:
        answer.append(div)
        if div != gcd_num**0.5:
            answer.append(gcd_num // div)

print(*sorted(answer))










