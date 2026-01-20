def solution(schedules, timelogs, startday):
    def to_min(t):
        return (t // 100) * 60 + (t % 100)

    answer = 0
    weekend = {5, 6}  # 0=월, 5=토, 6=일

    for i in range(len(schedules)):
        limit = to_min(schedules[i]) + 10
        ok = True

        for k in range(7):  # 시작일부터 7일
            weekday = (startday - 1 + k) % 7

            if weekday in weekend:
                continue

            if to_min(timelogs[i][k]) > limit:
                ok = False
                break

        if ok:
            answer += 1

    return answer
