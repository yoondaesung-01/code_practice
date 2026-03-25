def solution(num_list):
    sum_list = sum([s for s in num_list])**2
    mul_list = 1
    for i in num_list:
        mul_list*=i
    
    if mul_list < sum_list:
        return 1
    return 0