def solution(my_string):
    answer = my_string.strip().split(" ")
    return [s for s in answer if s != ""]