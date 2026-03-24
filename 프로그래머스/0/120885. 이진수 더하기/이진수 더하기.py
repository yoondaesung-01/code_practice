def solution(bin1, bin2):
    answer = ''
    num = int(bin1,2) + int(bin2,2)
    answer = bin(num)
    return answer[2:]