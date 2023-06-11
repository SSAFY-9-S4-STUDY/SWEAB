def solution(play_time, adv_time, logs):
    # 시간 단위를 초로 바꾸는 함수
    def time_to_num(time):
        time_sep = list(map(int, time.split(':')))
        return time_sep[0]*3600 + time_sep[1]*60 + time_sep[2]
    # 각 시간 당 시청자 수를 담을 배열
    N = time_to_num(play_time) + 1
    cum = [0] * N
    # 누적합 이용을 위해 시작 부분과 끝부분만 표시
    for log in logs:
        start, end = log.split('-')
        cum[time_to_num(start)] += 1
        cum[time_to_num(end)] -= 1
    # 기록해둔 시청기록 시작, 끝 지점을 통해 시간 당 시청자수의 누적합 구하기
    viewer = cum[0]
    for i in range(1, N):
        viewer += cum[i]
        cum[i] = cum[i-1] + viewer
    # 누적합을 통해 최대 시청 구간 구하기
    cum = [0] + cum
    video_len, max_value = time_to_num(adv_time), 0
    for i in range(N-video_len+1):
        tmp = cum[i+video_len] - cum[i]
        if tmp > max_value:
            max_value, time = tmp, i

    return f'{format(time//3600,"02")}:{format((time%3600)//60,"02")}:{format(time%60,"02")}'


play_time, adv_time = "02:03:55", "00:14:15"
logs = 	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))

