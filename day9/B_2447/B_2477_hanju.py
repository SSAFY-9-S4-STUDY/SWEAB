K = int(input())

lengths = [list(map(int,input().split())) for _ in range(6)]

rotation = lengths * 2
for i in range(9):
    if rotation[i][0] == rotation[i+2][0] and rotation[i+1][0] == rotation[i+3][0]:
        short_sides = [rotation[i][0], rotation[i+1][0]]
        long_sides = list(filter(lambda x: x[0] not in short_sides,lengths))
        total = long_sides[0][1] * long_sides[1][1]
        corner = rotation[i+1][1] * rotation[i+2][1]
        break

print((total - corner)*K)