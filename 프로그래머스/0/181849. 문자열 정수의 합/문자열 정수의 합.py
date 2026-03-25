def solution(num_str):
    num_list = []
    for i in range(0,len(num_str)):
        num_list.append(int(num_str[i]))
    return sum([s for s in num_list])