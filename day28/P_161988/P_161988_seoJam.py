# 펄스 수열의 합 중 큰 것 반환
def sum_pulse(sequence):
    sum_odd = sum_even = 0

    for idx in range(len(sequence)):
        if idx % 2:
            sum_odd += sequence[idx]
        else:
            sum_even += sequence[idx]

    return max(sum_odd, sum_even) - min(sum_odd, sum_even)


def solution(sequence):
    answer = -1e9

    for idx in range(len(sequence)):
        temp = list()

        while idx < len(sequence):
            temp.append(sequence[idx])
            answer = max(answer, sum_pulse(temp))
            idx += 1

    return answer


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))