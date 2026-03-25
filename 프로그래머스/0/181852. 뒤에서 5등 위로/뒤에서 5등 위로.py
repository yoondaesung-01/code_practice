def solution(num_list):
    num_list.sort()
    return [num_list[s] for s in range(5, len(num_list))]