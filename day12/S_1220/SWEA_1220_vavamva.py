# 붉은색 ==> S극 == y = 100 (아래로) <1>
# 파란색 ==> N극 == y = 0 (위로) <2>

import sys
sys.stdin = open("input_1220.txt")

for tc in range(1, 11):
    _ = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    count = 0
    for x in range(100):
        flag = 0
        for y in range(100):
            if table[y][x] == 1:
                flag = 1
            if flag and table[y][x] == 2:
                flag = 0
                count += 1
            
    print(f"#{tc} {count}")