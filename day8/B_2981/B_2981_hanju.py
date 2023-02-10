import sys

def common_divsor(n, m):
    res = []
    for i in range(1, int(n**0.5)+2):
        if n % i == 0:
            if i > m:
                res.append(i)
            if n // i > m:
                res.append(n // i)
    return res

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


N = int(sys.stdin.readline())
numbers = sorted([int(sys.stdin.readline()) for _ in range(N)])
min_value, second_value = numbers[0], numbers[1]

answer = []
# 두 번째값이 최솟값의 2배보다 크다면 최솟값 이상의 값부터 탐색
if second_value > min_value * 2:
    tmp = gcd(list(map(lambda x: x-min_value, numbers[1:])), N-1)
    if tmp > min_value:
        answer = common_divsor(tmp,min_value)


# 최솟값까지 탐색
m = [0] * (min_value+1)
for div in range(min_value,1,-1):
    if not m[div]:
        mod = min_value % div
        for i in range(1,N):
            if numbers[i] % div != mod:
                break
        else:
            for i in common_divsor(div,1):
                m[i] = 1


for i in range(2, min_value+1):
    if m[i]:
        answer.append(i)


tmp = 0
for i in sorted(answer):
    if i != tmp:
        print(i, end=' ')
        tmp = i









