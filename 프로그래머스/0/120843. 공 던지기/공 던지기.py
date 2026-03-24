def solution(numbers, k):
    answer = 0
    for i in range(k-1):
        if answer == len(numbers) -2:
            answer = 0
        elif answer == len(numbers)-1:
            answer = 1
        else:
            answer+=2
    return numbers[answer]