def solution(n):
    answer = []
    num = 2
    while num <= n:
        if n % num == 0:
            answer.append(num)
            n //= num
        else:
            num+=1
    answer = sorted(list(set(answer)))
    return answer