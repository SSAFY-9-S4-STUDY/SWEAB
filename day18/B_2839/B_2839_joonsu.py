N = int(input())
count = 0

while N > 0:
    if N == 1 or N == 2:
        N = -1
        count = -1
    elif N % 5 == 0:
        count += N // 5
        break
    else:
        N -= 3
        count += 1
print(count)