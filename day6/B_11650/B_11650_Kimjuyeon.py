
dots = []
N = int(input())
for i in range(N):
    dots.append(list(map(int,input().split())))

dots_sorted = sorted(dots, key = lambda x : (x[0], x[1]))

for _ in dots_sorted:
    print(f'{_[0]} {_[1]}')



