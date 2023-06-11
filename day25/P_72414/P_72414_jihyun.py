def solution(play_time, adv_time, logs):
    def str_to_sec(time_str):
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)

    def sec_to_str(time_sec):
        h = time_sec // 3600
        m = (time_sec % 3600) // 60
        s = (time_sec % 3600) % 60
        return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

    play_time_sec = str_to_sec(play_time)
    adv_time_sec = str_to_sec(adv_time)

    total_time = [0] * (play_time_sec + 1)

    for log in logs:
        start, end = log.split('-')
        start_sec = str_to_sec(start)
        end_sec = str_to_sec(end)
        total_time[start_sec] += 1
        total_time[end_sec] -= 1

    for i in range(1, play_time_sec + 1):
        total_time[i] += total_time[i - 1]

    for i in range(1, play_time_sec + 1):
        total_time[i] += total_time[i - 1]

    max_time = 0
    max_viewers = total_time[adv_time_sec - 1]

    for i in range(adv_time_sec, play_time_sec):
        if total_time[i] - total_time[i - adv_time_sec] > max_viewers:
            max_viewers = total_time[i] - total_time[i - adv_time_sec]
            max_time = i - adv_time_sec + 1

    answer = sec_to_str(max_time)
    return answer