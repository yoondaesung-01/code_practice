def solution(quiz):
    answer = []
    for i in quiz:
        temp = i.replace("=","==")
        if eval(temp):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer