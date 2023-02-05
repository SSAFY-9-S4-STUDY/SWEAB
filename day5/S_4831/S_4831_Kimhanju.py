import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    # 출발지와 종착지를 충전정류장 리스트에 저장
    stations = [0] + stations + [N]

    # 충전 가능 정류장끼리의 거리를 리스트로 저장
    distances = [stations[i+1] - stations[i] for i in range(M+1)]

    cnt, remain = 0, K  # 충전 횟수 초기값
    for d1, d2 in zip(distances[:M], distances[1:]):  # d1 = 다음 정류장까지의 거리, d2 = 다다음 정류장까지의 거리
        if d1 > K or d2 > K:  # 두 거리 중 하나라도 K보다 크면 종착점 도달 불가능
            cnt = 0
            break
        else:
            if remain < d1 + d2:  # 남은 기름으로 다다음 정거장까지 못 갈 경우
                cnt += 1  # 답 + 1
                remain = K  # 다음 정류장에서 기름 재충전
            else:
                remain -= d1  # 아니면 남은 기름에서 다음 정류장의 거리 차감

    print(f'#{test_case} {cnt}')






