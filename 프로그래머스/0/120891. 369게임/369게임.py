def solution(order):
    answer = sum([1 for i in str(order) if int(i)%3 ==0 and int(i)!=0])
    return answer