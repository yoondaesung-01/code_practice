def solution(polynomial):
    answer = []
    temp = polynomial.split(" + ")
    x= 0
    num=0
    for i in temp:
        if 'x' in i:
            a = i.replace("x","")
            x += int(a) if a else 1
        else:
            num += int(i)
    if x >=1:
        if x ==1:
            answer.append("x")
        else:
            answer.append(str(x)+"x")
    if num != 0:
        answer.append(str(num))
    return " + ".join(answer)