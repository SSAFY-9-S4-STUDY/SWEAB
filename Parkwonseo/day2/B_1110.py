N = int(input())
first_num = N

if N < 10:
    N = N * 11
else:
    N = ((N % 10) * 10) + (((N // 10) + (N % 10)) % 10)
i = 1

while N != first_num:
    N = ((N % 10) * 10) + (((N // 10) + (N % 10)) % 10)
    i = i + 1

print(i)
