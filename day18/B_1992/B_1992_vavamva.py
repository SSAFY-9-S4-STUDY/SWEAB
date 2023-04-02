"""
좌상 우상 좌하 우하 로 압축

0000 0000
0000 0000
0000 1111
0000 1111

0001 1111
0011 1111
0011 1111
0011 1111

(0 ? ? 1)
n은 2의 제곱수
== n // 2 로 계속해서 쪼갤 수 있다.
만약 0 또는 1로 이루어진 배열이 나오면 멈추고 저장.
n // 2 가 가능하면 괄호 하나 더

0000 00 00
0000 00 00

0000 11 11
0000 11 11

00 01 1111
00 11 1111

00 11 1111
00 11 1111

(0 (0011) (0?01) 1)
(0 (0011) (0(0111)01) 1)
"""


# def check(arr):
#     if sum(*arr)

def divide(n_, arr):
    n_ //= 2
    sub_1 = []
    sub_2 = []
    sub_3 = []
    sub_4 = []
    for i in range(n_):
        sub_1.append(arr[i][:n_])
        sub_2.append(arr[i][n_:])
        sub_3.append(arr[n_ + i][:n_])
        sub_4.append(arr[n_ + i][n_:])
    yield sub_1
    yield sub_2
    yield sub_3
    yield sub_4
    return
    # yield로 반환된 값은 map과 같이 위치 정보를 받아오기에,
    # (변수 정의 해주기 or list로 감싸기 등등)으로 해당 메모리 위치 참조를 해야 data를 알 수 있습니다.


def compress(n_, arr):
    global result
    if sum(sum(arr, [])) == n_ ** 2:
        result += "1"
    elif sum(sum(arr, [])) == 0:
        result += "0"
    else:
        result += "("
        sub_1, sub_2, sub_3, sub_4 = divide(n_, arr)
        compress(n_ // 2, sub_1)
        compress(n_ // 2, sub_2)
        compress(n_ // 2, sub_3)
        compress(n_ // 2, sub_4)
        result += ")"


n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, list(input()))))

result = ''
compress(n, table)
print(result)