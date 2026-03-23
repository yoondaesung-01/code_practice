def solution(n):
    answer = []
    for i in range(4, n+1):
        count = 0
        for j in range(1, int(i**0.5) +1):
            if i%j == 0:
                count+=1
                if count >= 2:
                    answer.append(i)
                    break
    return len(answer)