def solution(l, r):
    answer = []
    for i in range(l, r+1):
        for char in str(i):
            if char != "0" and char != "5":
                break 
        else:
            answer.append(i)
    return answer if answer else [-1]