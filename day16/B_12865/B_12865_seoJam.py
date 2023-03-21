import sys
sys.stdin = open("input.txt")

if __name__ == '__main__':
    n, k = map(int, input().split())  # n: 물품의 수, k: 버티는 최고 무게
    bag = []
    max_value = 0

    for _ in range(n):
        weight, value = map(int, input().split())
        bag.append((weight, value))

    # '가치' 순으로 내림차순 정렬
    bag.sort(key=lambda x: x[1], reverse=True)

    for i in range(n - 1):
        cnt = 1
        total_w = bag[i][0]
        total_v = bag[i][1]

        for j in range(i+1, n):
            if cnt == n or total_w + bag[j][0] > k: continue    # 무게 초과면 넘어가
            else:                                   # 무게 이하면 넣어
                cnt += 1
                total_w += bag[j][0]
                total_v += bag[j][1]
        # 다 끝나면 최고 가치 비교
        max_value = max(max_value, total_v)

    print(max_value)