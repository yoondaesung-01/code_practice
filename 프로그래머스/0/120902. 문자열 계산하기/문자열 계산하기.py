def solution(my_string):
    my_list = my_string.split(" ")
    cal = []
    answer= int(my_list[0])
    for i in range(1, len(my_list)):
        cal.append(my_list[i])
        if len(cal) == 2:
            if cal[0] == "+":
                answer += int(cal[1])
            else:
                answer -= int(cal[1])
            cal = []
    return answer