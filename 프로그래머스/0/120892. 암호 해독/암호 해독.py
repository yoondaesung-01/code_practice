def solution(cipher, code):
    answer = []
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            answer.append(cipher[i-1])
    answer = ''.join(answer)
    return answer