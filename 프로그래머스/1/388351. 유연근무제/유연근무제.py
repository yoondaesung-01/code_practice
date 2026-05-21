def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(timelogs)):
        time = schedules[i] + 10
        if time % 100 >= 60:
            time += 40
        is_correct = True
        for j in range(7):
            day = (startday + j) % 7 
            if day == 6 or day ==0:
                continue
            if timelogs[i][j] > time:
                is_correct = False
                break
        if is_correct ==True:
            answer+=1
    return answer