time = input()
exact_time = list(map(int, time.split()))
H = exact_time[0]
M = exact_time[1]

if H == 0 and M < 45:
    print(f'23 {60-(45-M)}')
elif M < 45:
    print(f'{H-1} {60-(45-M)}')
else:
    print(f'{H} {M-45}')