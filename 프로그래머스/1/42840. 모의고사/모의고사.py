def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for i in range(len(answers)):
        if num1[i%len(num1)] == answers[i]:
            count[0]+=1
        if num2[i%len(num2)] == answers[i]:
            count[1]+=1
        if num3[i%len(num3)] == answers[i]:
            count[2]+=1
    
    max_count = max(count)
    for idx, s in enumerate(count):
        if s == max_count:
            answer.append(idx + 1)    
    return answer