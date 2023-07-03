def solution(sequence):
    #  sum = 누적합 수열
    sum = [0] * (len(sequence)+1)
    for i in range(1, len(sequence)+1):
        sum[i] = sum[i-1] + sequence[i-1]*(-1)**(i-1)

    answer = max(sum) - min(sum)
    #  반대 펄스수열을 고려하지 않아도 되는 이유
    #  어차피 절댓값은 같기 때문

    return(answer)