# https://kimmimo.tistory.com/3

def solution(sequence):
    answer = 0
    sequence2 = sequence[:]
    pulse = 1

    for i in range(len(sequence)):
        sequence[i] *= pulse
        pulse *= -1
        sequence2[i] *= pulse

    max_sum = 0
    tmp = 0

    for s in sequence:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)

    tmp = 0

    for s in sequence2:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)

    answer = max_sum

    return answer