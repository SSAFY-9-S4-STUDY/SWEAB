n = int(input())
for y in range(n):
    for x in range(n):
        if x == y:
            print('#', end = '')
            if x == n - 1:
                print()
        if x != y:
            print('+', end = '')
            if x == n - 1:
                print()