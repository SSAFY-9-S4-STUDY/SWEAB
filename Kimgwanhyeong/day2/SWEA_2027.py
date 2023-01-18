N = 5
for i in range(N):
    for j in range(N):
        print_char = '#' if i == j else '+'
        print(print_char,end="")
    print()