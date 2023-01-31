number_of_paper = int(input())
total_paper = []
for y in range(100):
    tmp = []
    for x in range(100):
        tmp.append(0)
    total_paper.append(tmp)

for paper in range(number_of_paper):
    left, under = map(int, input().split())
    
    for fill_right in range(left, left + 10):
        for fill_top in range(under, under + 10):
            total_paper[fill_top][fill_right] = 1
    
result = sum(sum(total_paper, []))
print(result)