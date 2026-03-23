def solution(balls, share):
    def factorial(number):
        num = 1
        for i in range(1, number+1):
            num *= i
        return num
    n = factorial(balls)
    m = factorial(share)
    nm = factorial(balls-share)
    answer = n / (m * nm)
    return answer