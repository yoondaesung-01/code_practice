def solution(n):
    return sum(s for s in range(1, n+1) if n % s == 0) if n != 0 else 0