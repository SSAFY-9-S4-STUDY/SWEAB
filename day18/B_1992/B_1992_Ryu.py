import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, list(input().strip()))) for _ in range(N)]


def recursion(lst, N):  # small이상 big미만

    coco = lst[0][0]
    swi = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] != coco:
                swi = 1

    if swi == 1:
        print('(', end='')
        for nis, nib, njs, njb in [(0, N//2, 0, N//2), (0, N//2, N//2, N), (N//2, N, 0, N//2), (N//2, N, N//2, N)]:
            temp = [[lst[i][j] for j in range(njs,njb)] for i in range(nis, nib)]
            recursion(temp, N//2)
        print(')', end='')
    elif swi == 0:
        print(coco, end='')

recursion(lst, N)
print()