def solution(rectangles, cx, cy, ix, iy):
    arr = [[0]*51 for _ in range(51)]
    for x1, y1, x2, y2 in rectangles:
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                arr[y][x] = 1
    return arr

import pprint
rectangles = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
cx, cy, ix, iy = 1, 3, 7, 8

pprint.pprint(solution(rectangles, cx, cy, ix, iy), width=800)