N = int(input())

h = []

if N >= 100:
    for n in range(N + 1):
        if n >= 100:
            s = str(n)
            if 2 * int(s[1]) == int(s[0]) + int(s[2]):
                h.append(s)
    print(99 + int(len(h)))  
else:
    print(N)