# 브루트 포스 : 일일이 대입

N, M = map(int, input().split())
cards = list(map(int, input().split()))

close_num = []
# colab_min = 300000

# #1
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#             for k in range(j + 1, N):
#                 if cards[i] + cards[j] + cards[k] <= M:
#                     draw = M - cards[i] - cards[j] - cards[k]
#                     close_num.append(draw)

#2
# def black_jack(cards):
for i in range(N - 2):
    for j in range(N - 1):
            for k in range(N):
                if i == j or j == k or i == k:
                    continue
                elif cards[i] + cards[j] + cards[k] <= M:
                    draw = M - cards[i] - cards[j] - cards[k]
                    # yield draw
                    # if draw < colab_min:
                    #     colab_min = draw
                    close_num.append(draw)

# #3
# for i in cards[:-2]:
#     for j in cards[:-1]:
#         for k in cards:
#             if i == j or j == k or i == k:
#                 continue
#             elif i + j + k <= M:
#                 draw = M - i - j - k
#                 close_num.append(draw)

# result = M - min(black_jack(cards))
# print(M - min(black_jack(cards)))
print(M - min(close_num))
# print(M - colab_min)

# 1번 : 2번 : 3번 = 약 5 : 1 : 2