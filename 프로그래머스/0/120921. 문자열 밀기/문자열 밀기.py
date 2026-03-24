def solution(A, B):
    answer = -1
    count = 0
    def function(list):
        temp = []
        temp.append(list[len(list)-1])
        for i in range(len(list)-1):
            temp.append(list[i])
        temp = ''.join(temp)
        return temp
    for i in range(len(A)):
        if A == B:
            return count
        A = function(list(A))
        count += 1
    return answer