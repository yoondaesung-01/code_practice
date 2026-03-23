def solution(age):
    answer = []
    alphabet = 'abcdefghij'
    for i in str(age):
        answer.append(alphabet[int(i)])
    answer = ''.join(answer)
    return answer