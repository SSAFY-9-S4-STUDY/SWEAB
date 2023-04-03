import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

stack, cnt = [(0, 0, N, N)], [0, 0, 0]
while stack:
    r1, c1, r2, c2 = stack.pop()
    is_same, stop = paper[r1][c1], False

    for r in range(r1, r2):
        for c in range(c1, c2):
            if is_same != paper[r][c]:
                stop = True
                break
        if stop:
            part = (r2 - r1)//3
            for i in range(r1, r2, part):
                for j in range(c1, c2, part):
                    stack.append((i, j, i + part, j+part))       
            break
    else:
        cnt[is_same+1] += 1

for i in cnt:
    print(i)



