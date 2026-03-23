def solution(n):
    def factorial(num):
        temp = 1
        for i in range(1, num+1):
            temp *= i
        return temp
    answer = 10
    for i in range(1, 11):
        if factorial(i) > n:
            return i-1
    return answer