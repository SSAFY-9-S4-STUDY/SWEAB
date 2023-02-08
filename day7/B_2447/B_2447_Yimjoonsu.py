N = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']
    
    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)
    
    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(N)))

"""
도저히 모르겠어서 아래 페이지들 참고했습니다.
https://lucian-blog.tistory.com/57
https://sujeng97.tistory.com/11
"""