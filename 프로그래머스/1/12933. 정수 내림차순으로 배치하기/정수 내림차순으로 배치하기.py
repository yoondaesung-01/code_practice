def solution(n):
    return int("".join(s for s in sorted(str(n),reverse=True)))