def gcd(lst, n):
    while n != 1:

        small = min(lst[:2])
        big = max(lst[:2])
        lst = lst[2:]

        while big % small != 0:
            big, small = small, big % small
        else:
            lst.append(small)
            n -= 1

    return lst[0]

print(gcd([4,3],2))