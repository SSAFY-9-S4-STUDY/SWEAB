def solution(n, k, cmd):
    deleted = [0] * n
    for c in cmd:
        if c == 'C':
            deleted[k] = 1
            latest = k
        elif c == 'Z':
            deleted[latest] = 0
        else:
            o, r = c.split(" ")
            r = int(r) if o == 'D' else -int(r)
            print(r)

n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))