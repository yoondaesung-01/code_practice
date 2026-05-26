import math
from itertools import permutations
def solution(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i ==0: return False
        return True
    
    num_list = list(numbers)
    num_set = set()
    for i in range(1, len(numbers) +1 ):
        for p in permutations(num_list, i):
            num = int("".join(p))
            if is_prime(num):
                num_set.add(num)
    return len(num_set)