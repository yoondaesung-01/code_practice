def solution(numbers):
    answer = [-1] * len(numbers)
    my_list = []
    for i in range(len(numbers)):
        while my_list and numbers[my_list[-1]] < numbers[i]:
            index = my_list.pop()
            answer[index] = numbers[i]
        my_list.append(i)
    return answer