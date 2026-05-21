from collections import deque
def solution(cacheSize, cities):
    total_sum = 0
    q = deque()
    for city in cities:
        if cacheSize == 0:
            total_sum += 5
        else:
            if len(q) >= cacheSize:
                if city.lower() in q:
                    total_sum +=1
                    q.remove(city.lower())
                    q.append(city.lower())
                else:
                    total_sum +=5
                    q.popleft()
                    q.append(city.lower())
            else:
                if len(q) == 0:
                    total_sum +=5
                    q.append(city.lower())
                else:
                    if city.lower() in q:
                        total_sum+=1
                        q.remove(city.lower())
                        q.append(city.lower())
                    else:
                        total_sum+=5
                        q.append(city.lower())
    return total_sum