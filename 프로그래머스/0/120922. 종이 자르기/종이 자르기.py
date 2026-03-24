def solution(M, N):
    answer = 0
    if M != 1:
        answer += M-1
    if N != 1:
        answer += (N-1) * M
    
    return answer