C = int(input())

def average(n):
    return sum(n) / len(n)

for i in range(C):
    score_list = input().split()[1:]
    score_list_float = list(map(float, score_list))
    members = [score for score in score_list_float if score > average(score_list_float)]
    mem_percent = len(members) / len(score_list_float) * 100
    print(f'{mem_percent:.3f}%')

# score_list = []

# for i in range(C):
#     score_list.append(input().split()[1:])

# for m in score_list:
#     members = [float(n) for n in m if float(n) > average(m)]
#     mem_percent = round(len(members) / len(m) * 100, 3)
#     print(f'{mem_percent}%')
