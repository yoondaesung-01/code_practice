def solution(a, b, c, d):
    answer = 0
    my_list = [a, b, c, d]
    my_dict = {
        1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0
    }
    for key in my_dict.keys():
        if my_list.count(key):
            my_dict[key] = my_list.count(key)
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    p = sorted_dict[0][0] # 가장 많이 나온 숫자
    p_count = sorted_dict[0][1] # 가장 많이 나온 횟수

    # 두 번째로 많이 나온 정보
    q = sorted_dict[1][0]
    q_count = sorted_dict[1][1]

    # 세 번째 정보 (q, r 케이스용)
    r = sorted_dict[2][0]

    if p_count == 4:
        return 1111 * p
    elif p_count == 3:
        return (10 * p + q) ** 2
    elif p_count == 2:
        if q_count == 2:
            return (p + q) * abs(p - q)
        else:
            return q * r
    else:
        return min(my_list)
        
    return answer