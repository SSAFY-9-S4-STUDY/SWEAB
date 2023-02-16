def stars(n):
    if n == 1:
        return ['*']

    lst_star = stars(n // 3)
    want_lst = []

    for i in lst_star:
        want_lst.append(i * 3)
    for j in lst_star:
        want_lst.append(j + ' ' * (n //3) + j)
    for k in lst_star:
        want_lst.append(k * 3)

    return want_lst

N = int(input())

print('\n'.join(stars(N)))