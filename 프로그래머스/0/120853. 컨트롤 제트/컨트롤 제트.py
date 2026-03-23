def solution(s):
    zlist = s.split(" ")
    answer = 0
    temp = 0
    for i in zlist:
        if i == 'Z':
            answer -= temp
        else:
            answer+= int(i)
            temp = int(i)
    return answer