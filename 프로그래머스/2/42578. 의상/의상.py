from collections import Counter

def solution(clothes):
    counter = Counter([part for cloth, part in clothes])
    
    comb = 1
    for count in counter.values():
        comb *= (count + 1)
        
    return comb - 1