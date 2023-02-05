N = int(input())

spaces = set([])  # 중복되는 좌표값 제거를 위해 set 사용
for _ in range(N):
    R, C = map(int, input().split())  # 좌측하단 모서리 좌표값 입력
    for r in range(R, R+10):  # 100여개의 좌표값 spaces 에 추가
        for c in range(C, C+10):
            spaces.add((r, c))

# 좌표값 개수 = 색종이를 붙인 면적
print(len(spaces))