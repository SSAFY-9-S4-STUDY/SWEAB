from itertools import combinations


def stats(start, link):
    sum_s, sum_l = 0, 0
    for s_1, l_1 in zip(start, link):
        for s_2, l_2 in zip(start, link):
            sum_s += S[s_1][s_2]
            sum_l += S[l_1][l_2]
    return abs(sum_s - sum_l)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

diff = 10000
player = list(range(1, N))
for link_mem in combinations(player, N//2):
    start = [0]
    link = list(link_mem)
    start += set(player) - set(link)
    # start += [x for x in player if x not in link]

    diff = min(diff, stats(start, link))

print(diff)

