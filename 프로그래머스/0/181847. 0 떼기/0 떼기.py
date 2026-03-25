def solution(n_str):
    count = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            count = i
            break
    return n_str[count:]