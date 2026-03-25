def solution(str_list, ex):
    for i in range(len(str_list)):
        if str_list[i].find(ex)!= -1:
            str_list[i] = ''
    return ''.join(str_list)