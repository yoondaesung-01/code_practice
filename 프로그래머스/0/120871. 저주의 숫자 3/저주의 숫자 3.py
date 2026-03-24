def solution(n):
    answer = 0
    temp = []
    for i in range(1, 300):
        if i%3==0 or str(i).find("3")!=-1:
            i+=1
        else:
            temp.append(i)
        if len(temp) == n:
            break
    answer = temp.pop()
    return answer