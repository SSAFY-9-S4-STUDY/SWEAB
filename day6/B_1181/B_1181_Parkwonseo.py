N = int(input())

# 입력이 개행으로 구분
quest = []
for i in range(N):
    tmp = input()
    if tmp not in quest:
        quest.append(tmp)

# 길이 sort
# quest.sort(key = lambda x: len(x))
# print(quest)

# 같은 길이 내에서 사전적 sort
"""
l = r = 0
for idx in range(1, len(quest) - 1):
    if len(quest[idx]) != len(quest[idx - 1]) and len(quest[idx]) == len(quest[idx + 1]):
        l = idx
    elif len(quest[idx]) != len(quest[idx + 1]) and len(quest[idx]) == len(quest[idx - 1]):
        r = idx
        quest[l:r + 1].sort()
맨 처음과 맨 끝 못찾음, 얕복은 메모리 및 시간 많이 먹음
"""

# sort 한번에 두개의 조건은 안될까?
quest = sorted(quest, key = lambda x: (len(x), x))

print(*quest, sep="\n")