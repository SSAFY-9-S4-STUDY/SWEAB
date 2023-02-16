def i_will(go_to):
    if go_to[0] == 1:
        return 4
    elif go_to[0] == 2:
        return 3
    elif go_to[0] == 3:
        return 1
    elif go_to[0] == 4:
        return 2
    

k = int(input())

go = [list(map(int, input().split())) for _ in range(6)]
point = []

""" 처음의 코드
for i in range(5):
    if i_will(go[i]) != go[i + 1][0]:
        point.append(go[i])
        point.append(go[i + 1])

인덱스 끝에서 반대방향으로 트는 부분이 생기면
"point" 변수엔 아무것도 할당되지 않는다.
"""


for i in range(-1, 5): # 끝 인덱스에서 꺾이는 경우를 찾아줄 수 있다.
    if i_will(go[i]) != go[i + 1][0]:
        point.append(go[i])
        point.append(go[i + 1])

longest = (0, 0)
for i in range(6):
    if longest[1] < go[i][1]:
        longest = go[i]

second = 0

if longest[0] <= 2:
    for i in range(6):
        if go[i][0] >= 3:
            if second < go[i][1]:
                second = go[i][1]
elif longest[0] >= 3:
    for i in range(6):
        if go[i][0] <= 2:
            if second < go[i][1]:
                second = go[i][1]

minus = point[0][1] * point[1][1]

print((longest[1] * second - minus) * k)
