num = []
tmp = ''
plus = False

for x in input():
    if x.isdigit():
        tmp += x
        continue
    if plus:
        num[-1] += int(tmp)
    else:
        num.append(int(tmp))
    tmp = ''
    plus = True if x == '+' else False

if plus:
    num[-1] += int(tmp)
else:
    num.append(int(tmp))

ans = num.pop(0)
while num:
    ans -= num.pop()

print(ans)