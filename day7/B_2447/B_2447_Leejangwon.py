# 이번에도 재귀함수 땜에 고생하네요...
# 아이디어를 가지고 있었는데 이를 구현하는데 있어서 어려움이 있었어요.
# 특히, 하나의 unit을 사람이 하는 거처럼 옆에 붙일 수 있을 거라 생각했는데... 이는 사실상 어렵지 않나..
# 그리고 join을 통해 리스트 기호를 빼낼 수 있다는 것을 알았어요.. 재귀함수는 좀 더 연습해보도록 하겠습니당...


def star(n):
    if n == 1:
        return ['*']

    stars = star(n//3)
    mw = []

    for s in stars:
        mw.append(s * 3)
    for s in stars:
        mw.append(s + ' '*(n//3) + s)
    for s in stars:
        mw.append(s * 3)

    return mw

N = int(input())
print('\n'.join(star(N)))