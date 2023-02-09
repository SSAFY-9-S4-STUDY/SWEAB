# 제가 문제번호를 잘못 봐서 2477 문제를 풀었어요ㅠㅠ
# 이문제 나중에 풀어보고 싶으시면 피드백은 넘겨주시면 되욤 

melon = int(input())

# 아이디어2: 방향과 길이를 튜플로 묶고 오름차순으로 정렬하여 앞 세 개 중 가운데 튜플의 방향이 1이면 방향이 2인 튜플이 긴 가로
# 뒤 세 개 중 가운데 튜플의 방향이 3이면 방향이 4인 튜플이 긴 세로
# 근데 틀림. 왜? 짧은 변들의 순서도 중요. ->
length_lst = []
for _ in range(6):
    dir, length = tuple(map(int, input().split()))
    length_lst.append((dir,length))


# 아이디어4: index - 1, index 숫자에 따라서 생기는 모양을 딕셔너리에 저장
shape_dic = {(1, 3): 'a', (2, 4): 'b', (3, 2): 'c', (4, 1): 'd'}
max_area = rest_area = 0
for idx in range(6):
    if shape_dic.get((length_lst[idx-1][0], length_lst[idx][0])):
        rest_area = length_lst[idx-1][1] * length_lst[idx][1]
        max_area = length_lst[idx-4][1] * length_lst[idx-3][1]
        area = max_area - rest_area
        break

print(area * melon)