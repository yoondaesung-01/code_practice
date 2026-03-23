def solution(numbers):
    numbers.sort()
    if numbers[-1] * numbers[-2] > numbers[0] * numbers[1]:
        answer = numbers[-1] * numbers[-2]
    else:
        answer = numbers[0] * numbers[1]
    return answer