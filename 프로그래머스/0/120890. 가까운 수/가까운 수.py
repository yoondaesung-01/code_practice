def solution(array, n):
    temp = abs(array[0]-n)
    num = array[0]
    for i in range(1,len(array)):
        if abs(array[i]-n) <= temp:
            if abs(array[i]-n) == temp:
                if num > array[i]:
                    num = array[i]
                    temp = abs(array[i]-n)
            else:
                temp = abs(array[i]-n)
                num = array[i]
    return num