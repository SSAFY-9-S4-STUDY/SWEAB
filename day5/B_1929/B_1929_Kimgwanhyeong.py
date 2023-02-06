m, n = map(int, input().split())

import math
def is_prime_num(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for trial in range(m, n + 1):
        if is_prime_num(trial):
            print(trial)

# 백준 제출은 틀렸습니다.
# 이유가 무엇 때문인지 궁금합니다.