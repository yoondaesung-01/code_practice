def solution(rsp):
    answer = []
    dict = { "2" : "0", "0" : "5", "5" : "2"}
    for i in rsp:
        answer.append(dict[i])
    answer = "".join(answer)
    return answer