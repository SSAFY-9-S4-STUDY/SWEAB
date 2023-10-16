# Googling 했습니다...
from itertools import permutations

def solution(n, weak, dist):
    m = len(weak)
    for i in range(m):
        weak.append(weak[i] + n)
    # 모든 친구 동원
    answer = len(dist) + 1

    for start in range(m):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[0]

            for i in range(start, start + m):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                        
                    position = weak[i] + friends[count-1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    return answer