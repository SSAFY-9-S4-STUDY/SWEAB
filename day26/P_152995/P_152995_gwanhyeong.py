def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key=lambda x:(-x[0], x[1]))
    max_test = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        
        if score[1] >= max_test:
            max_test = score[1]
            if sum(score) > wanho_sum:
                answer += 1
                
    return answer