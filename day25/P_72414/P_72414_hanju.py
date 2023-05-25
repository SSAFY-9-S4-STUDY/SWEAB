def solution(play_time, adv_time, logs):
    # 시간 단위를 초로 바꾸는 함수
    def time_to_num(time):
        time_sep = list(map(int, time.split(':')))
        return time_sep[0]*3600 + time_sep[1]*60 + time_sep[2]
    # 각 시간 당 시청자 수를 담을 배열
    N = time_to_num(play_time) + 1
    viewers = [0] * N
    # 누적합 이용을 위해 시작 부분과 끝부분만 표시
    for log in logs:
        start, end = log.split('-')
        viewers[time_to_num(start)] += 1
        viewers[time_to_num(end)] -= 1
    # 기록해둔 시청기록 시작, 끝 지점을 통해 시간 당 시청자수의 누적합 구하기
    current = viewers[0]
    for i in range(1, N):
        current += viewers[i]
        viewers[i] += viewers[i-1] + current
    # 누적합을 통해 최대 시청 구간 구하기
    viewers = [0] + viewers
    print(viewers)



play_time, adv_time = "02:03:55", "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))

