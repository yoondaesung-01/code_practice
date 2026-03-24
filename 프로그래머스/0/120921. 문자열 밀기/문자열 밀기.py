def solution(A, B):
    answer = 0
    def function(list):
        temp = []
        temp.append(list[len(list)-1])
        for i in range(len(list)-1):
            temp.append(list[i])
        temp = ''.join(temp)
        return temp
    for i in range(len(A)):
        if A == B:
            return answer
        A = function(list(A))
        answer += 1
    return -1