def solution(sequence):
    answer = -100000
    prefix_one = prefix_two = 0
    prefix_one_min = prefix_two_min = 0
    pulse = 1

    for num in sequence:
        prefix_one += num * pulse
        prefix_two += num * (-pulse)

        answer = max(answer,
                     prefix_one-prefix_one_min,
                     prefix_two - prefix_two_min)

        prefix_one_min = min(prefix_one_min, prefix_one)
        prefix_two_min = min(prefix_two_min, prefix_two)

        pulse *= -1
    return answer        
        