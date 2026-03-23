def solution(array):
    answer = 0
    for i in array:
        answer+= int(str(i).count(str(7)))
    return answer