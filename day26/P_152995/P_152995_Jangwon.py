def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    bp = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if bp <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            bp = score[1]
    return answer

# def solution(scores):
#     target = [scores[0][0], scores[0][1], scores[0][0] + scores[0][1]]  # 원호의 점수
#
#     new_scores = sorted(list(map(lambda x: [x[0], x[1], x[0] + x[1]], scores)), key=lambda x : (-x[2], -x[0], x[1]))
#
#     answer = 1  # 순위를 카운트하는 변수
#     bp = new_scores[0]
#     for score in new_scores:
#         if target[0] < score[0] and target[1] < score[1]: # 원호가 인센티브를 못받을 때.
#             answer = -1
#             break
#         if score[2] == target[2]:  # 총합이 같기에 동점자고 내림차순 정렬이므로 더 이상 판단 안해도 됨.
#             break
#         if score == target:  # 원호 본인 position에 왔음.
#             break
#         # 이 아래에는 인센티브 못받는 애들이랑 순위 카운트해야함.
#         if bp[0] > score[0] and bp[1] > score[1]: # 인센티브 못받는 애들 거르기
#             continue
#         else:  # 인센티브 받을 수 있는 사람들 중
#             if score[2] > target[2]:  # 원호의 총합이 더 작다면
#                 answer += 1  # 순위 카운트 변수에 1 더해줌
#     return answer
#
# print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))