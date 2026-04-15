def solution(rank, attendance):
    new_list = [(rk, i) for i, (rk, at) in enumerate(zip(rank, attendance)) if at]
    top_3= sorted(new_list, key=lambda x: x[0])[:3]
    result = [item[1] for item in top_3]
    return result[0] * 10000 + result[1] * 100 + result[2]