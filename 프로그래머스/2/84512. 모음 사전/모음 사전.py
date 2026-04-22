from itertools import permutations

def solution(word):
    aeiou = ['A','E','I','O','U']
    words_list = []
    
    def dfs(current):
        if len(current) > 5:
            return
        if current:
            words_list.append(current)
        
        for letter in aeiou:
            dfs(current + letter)
    
    dfs("")

    return words_list.index(word) + 1
