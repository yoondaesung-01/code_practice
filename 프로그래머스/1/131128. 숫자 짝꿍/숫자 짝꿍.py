def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        str_i = str(i)
        count_X = X.count(str_i)
        count_Y = Y.count(str_i)
        answer+= str_i * min(count_X, count_Y)
    if answer == '':
        return "-1"
    
    if answer[0] == "0":
        return "0"
    return answer