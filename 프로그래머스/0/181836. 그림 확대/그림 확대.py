def solution(picture, k):
    answer = []
    for row in picture:
        new_row = "".join(p * k for p in row)
        answer.extend([new_row] * k)
    return answer