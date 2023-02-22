def count_twos(num):
    count = 0
    while num != 0:
        num = num // 2
        count += num
    return count


def count_fives(num):
    count = 0
    while num != 0:
        num = num // 5
        count += num
    return count


N, M = map(int, input().split())
result = 0
if M:
    result = min(count_twos(N) - count_twos(M) - count_twos(N-M),\
                 count_fives(N) - count_fives(M) - count_fives(N-M))

print(result)