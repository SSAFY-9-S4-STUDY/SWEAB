# final
def hanoi(N, start, path, end):
    if N == 1:
        print(f'{start} {end}')

    elif N > 1:
        hanoi(N-1, start, end, path)
        print(f'{start} {end}')
        hanoi(N-1, path, start, end)

N = int(input())
print(2 ** N -1) # 문제 잘 읽기; 출력값 파악 잘할것
hanoi(N, 1, 2, 3)

