def solution(common):
    answer = 0
    logic1 = common[1]-common[0]
    logic2 = common[2]-common[1]
    if logic1 == logic2:
        answer = common[len(common)-1] + logic1
    else:
        answer = common[len(common)-1] * (common[1]/common[0])
    return answer