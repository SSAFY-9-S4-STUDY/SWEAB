A, B, C = map(int, input().split())

mod, ans = A % C, 1
for i in bin(B)[::-1][:-2]:
    if i == '1':
        ans = (ans * mod) % C
    mod = (mod * mod) % C

print(ans)
