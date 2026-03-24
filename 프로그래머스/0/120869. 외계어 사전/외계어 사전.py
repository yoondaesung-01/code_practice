def solution(spell, dic):
    for i in dic:
        count = 0
        for j in spell:
            if i.find(j) == -1:
                continue
            else:
                count+=1
        if count == len(spell):
            return 1
    return 2