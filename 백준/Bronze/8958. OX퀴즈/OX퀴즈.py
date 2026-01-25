N = int(input())

for i in range(N):
    char = input()
    
    score = 0
    bonus = 0
    
    for j in char:
        if j == 'O':
            bonus += 1
            score += bonus
        else:
            bonus = 0
            
    print(score)