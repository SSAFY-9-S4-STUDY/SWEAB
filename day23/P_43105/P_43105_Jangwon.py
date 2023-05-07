def solution(triangle):
    for i in range(len(triangle) - 1, 0, -1): # triangle 배열을 역으로 보면서
        for j in range(len(triangle[i]) - 1):  # 해당 배열에서는 다음 배열과의 숫자를 비교하여
            if triangle[i][j] <= triangle[i][j + 1]:  # 한쪽이 더 큰 쪽에
                triangle[i - 1][j] += triangle[i][j + 1] # 다음 순회할 배열의 해당 인덱스 값에 더해준다.(누적해서 더해주는 아이디어)
            else:
                triangle[i - 1][j] += triangle[i][j]
    answer = triangle[0][0]
