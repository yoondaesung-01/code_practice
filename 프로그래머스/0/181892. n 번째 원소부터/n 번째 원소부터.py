def solution(num_list, n):
    answer = [num_list[s] for s in range(n-1, len(num_list))]
    return answer