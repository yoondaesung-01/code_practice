def solution(name, yearning, photo):
    answer = []
    
    score = dict(zip(name, yearning))
    
    for p in photo:
        result = 0
        for person in p:
            result += score.get(person, 0)
        answer.append(result)
    
    return answer
