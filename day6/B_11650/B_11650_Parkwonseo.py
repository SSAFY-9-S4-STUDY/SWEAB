# 좌표 정렬하기
import time
start = time.time()  # 시작 시간 저장

N = int(input())
coor = [] # coordinate: 좌표
for _ in range(N):
    tmp = list(map(int, input().split()))
    coor.append(tmp)

# 버블 정렬
# for i in range(N - 1, 0, -1):
#     for j in range(i):
#         if coor[j][0] > coor[i][0]:
#             coor[j], coor[j + 1] = coor[j + 1], coor[j]
#         elif coor[j][0] == coor[i][0] and coor[j][1] > coor[i][1]:
#             coor[j], coor[j + 1] = coor[j + 1], coor[j]

# 시간 초과 떴습니다~ 다 해산해주세요~

coor = sorted(coor, key = lambda x: (x[0]))
counting = [0] * 200001
for i in range(N):
    counting[i] = coor[i][0] + 100000


for i in coor:
    print(i[0], i[1])
print("time :", time.time() - start)
# coor = sorted(coor, key = lambda x: (x[0] + 100000) * 1000000 + x[1] + 100000)