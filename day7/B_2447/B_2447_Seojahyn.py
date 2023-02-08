from sys import stdin
stdin = open("input.txt")

def input():
    return stdin.readline().rstrip()

def stars(N):
    n = N//3
    if n == 1:
        return print('*'*3, '* *', '*'*3, sep= '\n')

    else:
        stars(n) * n, stars(n)


N = int(input())
stars(9)


def star(N):
    n = N//3
    return print('*' * 3 * n, '* *' * n, '*' * 3 * n, sep = '\n')

star(9)