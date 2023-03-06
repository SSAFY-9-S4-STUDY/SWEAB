# 최대 성적표 만들기

t = int(input())
for tc in range(1, t + 1):
    total, view = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)

    result = 0
    for i in range(view):
        result += score[i]

    print(f"#{tc} {result}")