
parent = [[(r, c) for c in range(51)] for r in range(51)]
cells = [['EMPTY']*51 for _ in range(51)]
result = []

def find(r, c):
    if (r, c) == parent[r][c]:
        return parent[r][c]
    pr, pc = parent[r][c]
    parent[r][c] = find(pr, pc)
    return parent[r][c]

def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]

def UPDATE1(r, c, value):
    pr, pc = find(r, c)
    cells[pr][pc] = value

def UPDATE2(value1, value2):
    for r in range(51):
        for c in range(51):
            pr, pc = find(r,c)
            if cells[pr][pc] == value1:
                cells[pr][pc] = value2

def MERGE(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    if (r1, c1) == (r2, c2):
        return 
    if cells[r1][c1] != "EMPTY" :
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)

def UNMERGE(r, c):
    pr, pc = find(r, c)
    value = cells[pr][pc]

    merge_list = ()
    for r1 in range(51):
        for c1 in range(51):
            r2, c2 = find(r1, c1)
            if (r2, c2) == (pr, pc):
                merge_list.append((r1, c1))
    
    for r1, c1 in merge_list : 
        parent[r1][c1] = (r1, c1)
        if (r1, c1) != (r, c):
            cells[r1][c1] = "EMPTY"
        else :
            cells[r1][c1] = value

def PRINT(r, c):
    pr, pc = find(r, c)
    result.appent(cells[pr][pc])

def solution(commands):
    for command in commands:
        func, *msg = command.split()
        if func == "UPDATE":
            if len(msg) == 3:
                r, c, value = msg
                UPDATE1(int(r), int(c), value)
            else:
                value1, value2 = msg
                UPDATE2(value1, value2)
        elif func == "MERGE":
            r1, c1, r2, c2 = msg
            MERGE(int(r1), int(c1), int(r2), int(c2))
        elif func == "UNMERGE":
            r, c = msg
            UNMERGE(int(r), int(c))
        else : 
            r, c = msg
            PRINT(int(r), int(c))

    return result

