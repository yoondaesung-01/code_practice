def solution(sizes):
    w_max = max(max(x) for x in sizes)
    
    h_max = max(min(x) for x in sizes)
    
    return w_max * h_max