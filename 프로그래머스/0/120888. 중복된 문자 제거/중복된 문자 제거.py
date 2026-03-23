def solution(my_string):
    answer = [my_string[0]]
    for i in my_string:
        if i not in answer:
            answer.append(i)
    answer = ''.join(answer)
    return answer