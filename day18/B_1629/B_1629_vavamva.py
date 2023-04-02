number, square, div = map(int, input().split())

# div로 나눈 나머지를 구할겁니다.

lst = []
while square > 0:
    tmp = number % div
    square -= 1
    if tmp in lst:
        lst.append(tmp)
        break
    lst.append(tmp)
    number *= tmp
    # print(f"tmp: {tmp}")

if square > 0:
    while lst:
        now = lst.pop(0)
        if lst[-1] == now:  # 반복의 첫 시작지점을 끝으로 옮겼음
            break
    # print(f"end_remain: {square}")
    idx = square % len(lst)
    print(lst[idx - 1])  # 한 차례씩 밀린 lst 이므로 idx -1 필요
else:
    print(tmp)
