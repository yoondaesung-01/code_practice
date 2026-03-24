def solution(chicken):
    temp = []
    while chicken // 10 > 0:
        temp.append(chicken //10)
        chicken = chicken //10 + chicken%10
    
    return sum(s for s in temp)