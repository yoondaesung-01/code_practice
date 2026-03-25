def solution(myString):
    answer = []
    mylist = myString.split("x")
    for i in mylist:
        answer.append(len(i))
    return answer