def solution(bandage, health, attacks):
    max_health, count = health, 0
    atk_index = 0
    for i in range(1, attacks[-1][0] + 1):
        if attacks[atk_index][0] == i:
            health -= attacks[atk_index][1]
            count = 0
            atk_index+=1
            if health <= 0:
                return -1
            continue
        count+=1
        health = min(max_health, health+bandage[1])
        if count == bandage[0]:
            health = min(max_health, health+bandage[2])
            count = 0
    return health