def solution(myString, pat):
    table = str.maketrans({'A': 'B', 'B': 'A'})
    myString = myString.translate(table)
    if pat in myString:
        return 1
    return 0