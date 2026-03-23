def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str)//n+1):
        if (i+1)*n <= len(my_str):
            answer.append(my_str[i*n : (i+1)*n])
        else:
            if len(my_str) % i*n <= n and len(my_str) % (i * n) !=0:
                answer.append(my_str[i*n: len(my_str)])
    return answer