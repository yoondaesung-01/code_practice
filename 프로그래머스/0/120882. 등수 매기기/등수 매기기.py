def solution(score):
    temp = [s[0]+s[1] for s in score]
    sorted_temp = sorted(temp, reverse = True)
    answer = [sorted_temp.index(i) + 1 for i in temp]
    return answer