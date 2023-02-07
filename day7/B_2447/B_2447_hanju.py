def star(n):
    if n == 3:
        return '***\n* *\n***'
    else:
        star_split = star(n//3).split('\n')
        updown = list(map(lambda x: x*3, star_split))
        mid = list(map(lambda x: x + ' ' * (n//3) + x,star_split ))
        return '\n'.join(updown + mid + updown)

print(star(int(input())))