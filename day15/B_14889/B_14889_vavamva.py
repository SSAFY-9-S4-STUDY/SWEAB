# 스타트와 링크
import itertools

# n = 2 * k
# S : 시너지 // Sij + Sji
# team : 스타트팀, 링크팀
# 밸런스 맞게 팀 짜기 : team_s & team_l 의 차이가 가장 작게 팀 짜기


def team(num):
    player = list(range(1, num + 1))
    cases = list(itertools.combinations(player, num // 2))
    # start 팀을 정하면 link팀이 정해지고, 팀을 변경할 필요 없이 차이만 작으면 된다
    team_1 = cases[:len(cases) // 2]
    yield team_1
    team_2 = list(reversed(cases[len(cases) // 2:]))
    yield team_2

    return


def find_interval(num):
    team_s = 0
    team_l = 0

    synergy_s = list(itertools.combinations(available[0][num], 2))
    synergy_l = list(itertools.combinations(available[1][num], 2))

    for player in synergy_s:
        team_s += table[player[0]][player[1]] + table[player[1]][player[0]]
    for player in synergy_l:
        team_l += table[player[0]][player[1]] + table[player[1]][player[0]]

    return abs(team_s - team_l)


n = int(input())
# index를 사람의 숫자로 맞추기 위한 패딩
table = [[0] + list(map(int, input().split())) for _ in range(n)]
table = [[0] * (n + 1)] + table

available = list(team(n))
num_of_cases = len(available[0])

min_interval = 200 * 20

for idx in range(num_of_cases):
    tmp = find_interval(idx)
    if min_interval > tmp:
        min_interval = tmp

print(min_interval)